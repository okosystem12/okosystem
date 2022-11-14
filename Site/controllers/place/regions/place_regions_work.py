import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.log.log import log
from Site.app.object.elem import elem
from Site.models import Countries, Regions


@csrf_exempt
def place_regions_work(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        id = elem(_data, 'id', None)
        country_id = elem(_data, 'country_id', None)
        title = elem(_data, 'title')
        country = Countries.objects.filter(Q(removeAt=None) & Q(pk=country_id)).first()
        _old = None
        if country:
            if not Regions.objects.filter(Q(removeAt=None) & Q(country=country) & Q(title=title)).exclude(
                    Q(pk=id)).exists():
                _new = False
                region = Regions.objects.filter(Q(removeAt=None) & Q(pk=id)).first()
                if not region:
                    _new = True
                    region = Regions.objects.create()
                else:
                    _old = region

                region.country = country
                region.title = title
                region.save()

                regionsList = Regions.objects.filter(Q(removeAt=None) & Q(pk=region.pk))

                if _new:
                    log(request.user.pk, 'Настройки', 'Создание', 'Регион')
                else:
                    if _old:
                        log(request.user.pk, 'Настройки', 'Изменение', 'Регион')

                args = {
                    'successText': 'Запись обновлена' if _new else 'Запись добавлена',
                    'regionsList': list(regionsList.values()),
                }
            else:
                args = {
                    'errorHighlight': 'Регион с названием "' + title + '" для страны "' + country.title + '" уже присутствует в системе',
                }
        else:
            args = {
                'errorText': 'Ошибка',
            }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

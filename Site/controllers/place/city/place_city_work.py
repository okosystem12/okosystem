import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.log.log import log
from Site.app.object.elem import elem
from Site.models import Countries, Regions, Cities


@csrf_exempt
def place_city_work(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        id = elem(_data, 'id', None)
        country_id = elem(_data, 'country_id', None)
        region_id = elem(_data, 'region_id', None)
        title = elem(_data, 'title')
        country = Countries.objects.filter(Q(removeAt=None) & Q(pk=country_id)).first()
        _old = None
        if country:
            region = Regions.objects.filter(Q(removeAt=None) & Q(pk=region_id)).first()
            if Cities.objects.filter(Q(removeAt=None) & Q(country=country) & Q(region=region) & Q(title=title)).exclude(
                Q(pk=id)).count() == 0:
                _new = False
                city = Cities.objects.filter(Q(removeAt=None) & Q(pk=id)).first()
                if not city:
                    _new = True
                    city = Cities.objects.create()
                else:
                    _old = city

                city.country = country
                city.region = region
                city.title = title
                city.save()

                citiesList = Cities.objects.filter(Q(removeAt=None) & Q(pk=city.pk))

                if _new:
                    log(request.user.pk, 'Настройки', 'Создание', 'Город')
                else:
                    if _old:
                        log(request.user.pk, 'Настройки', 'Изменение', 'Город', _old.__dict__)

                args = {'successText': 'Запись обновлена' if _new else 'Запись добавлена',
                    'citiesList': list(citiesList.values()), }
            else:
                args = {'errorHighlight': 'Город с названием "' + title + '" для страны "' + country.title + (
                    ('" и региона "' + region.title) if region else '') + '" уже присутствует в системе', }
        else:
            args = {'errorText': 'Ошибка', }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.object.elem import elem
from Site.models import Countries, Regions


@csrf_exempt
def place_regions_work(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        id = elem(_data, 'id', None)
        country_id = elem(_data, 'country_id', None)
        title = elem(_data, 'title')
        country = Countries.objects.filter(Q(removeAt=None) & Q(pk=country_id)).first()
        if country:
            if Regions.objects.filter(Q(removeAt=None) & Q(country=country) & Q(title=title)).exclude(
                    Q(pk=id)).count() == 0:
                _new = False
                region = Regions.objects.filter(Q(removeAt=None) & Q(pk=id)).first()
                if not region:
                    _new = True
                    region = Regions.objects.create()

                region.country = country
                region.title = title
                region.save()

                regionsList = Regions.objects.filter(Q(removeAt=None) & Q(pk=region.pk))

                args = {
                    'successText': 'Запись обновлена' if _new else 'Запись добавлена',
                    'regionsList': list(regionsList.values()),
                }
            else:
                args = {
                    'errorText': 'Регион с названием "' + title + '" для страны "' + country.title + '" уже присутствует в системе',
                }
        else:
            args = {
                'errorText': 'Ошибка',
            }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

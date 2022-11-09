import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.log.log import log
from Site.app.object.elem import elem
from Site.models import Countries


@csrf_exempt
def place_countries_work(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        id = elem(_data, 'id', None)
        title = elem(_data, 'title')
        _old = None
        if not Countries.objects.filter(Q(removeAt=None) & Q(title=title)).exclude(Q(pk=id)).exists():
            _new = False
            country = Countries.objects.filter(Q(removeAt=None) & Q(pk=id)).first()
            if not country:
                _new = True
                country = Countries.objects.create()
            else:
                _old = country
            country.title = title
            country.save()

            countriesList = Countries.objects.filter(Q(removeAt=None) & Q(pk=country.pk))

            if _new:
                log(request.user.pk, 'Настройки', 'Создание', 'Страна')
            else:
                if _old:
                    log(request.user.pk, 'Настройки', 'Изменение', 'Страна', _old.__dict__)

            args = {
                'successText': 'Запись обновлена' if _new else 'Запись добавлена',
                'countriesList': list(countriesList.values()),
            }
        else:
            args = {
                'errorHighlight': 'Страна с названием "' + title + '" уже присутствует в системе',
            }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

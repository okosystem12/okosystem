import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.log.log import log
from Site.app.object.elem import elem
from Site.models import Vch


@csrf_exempt
def vch_work(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        id = elem(_data, 'id', None)
        number = elem(_data, 'number')
        _old = None
        if not Vch.objects.filter(Q(removeAt=None) & Q(number=number)).exclude(Q(pk=id)).exists():
            _new = False
            _vch = Vch.objects.filter(Q(removeAt=None) & Q(pk=id)).first()
            if not _vch:
                _new = True
                _vch = Vch.objects.create()
            else:
                _old = _vch

            _vch.number = number
            _vch.save()

            if _new:
                log(request.user.pk, 'Настройки', 'Создание', 'ВЧ')
            else:
                if _old:
                    log(request.user.pk, 'Настройки', 'Изменение', 'ВЧ')

            args = {
                'successText': 'Запись обновлена' if not _new else 'Запись добавлена',
            }
        else:
            args = {
                'errorHighlight': 'ВЧ с номером "' + number + '" уже присутствует в системе',
            }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

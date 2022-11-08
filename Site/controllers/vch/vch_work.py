import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
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

        if Vch.objects.filter(Q(removeAt=None) & Q(number=number)).exclude(Q(pk=id)).count() == 0:
            _new = False
            _vch = Vch.objects.filter(Q(removeAt=None) & Q(pk=id)).first()
            if not _vch:
                _new = True
                _vch = Vch.objects.create()

            _vch.number = number
            _vch.save()

            args = {
                'successText': 'Запись обновлена' if _new else 'Запись добавлена',
            }
        else:
            args = {
                'errorHighlight': 'ВЧ с номером "' + number + '" уже присутствует в системе',
            }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

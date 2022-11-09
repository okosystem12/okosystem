import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.log.log import log
from Site.app.object.elem import elem
from Site.app.object.object import objectRemoveAt
from Site.models import ControlUser


@csrf_exempt
def control_remove(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))
    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        _id = elem(_data, 'id', None)
        cList = ControlUser.objects.filter(Q(pk=_id))
        objectRemoveAt(cList)
        log(request.user.pk, 'Данные ЛС', 'Удаление', '', list(cList.values()))

        args['successText'] = 'Запись удалена'
        args['reload'] = True
    return HttpResponse(json.dumps(args, default=my_convert_datetime))

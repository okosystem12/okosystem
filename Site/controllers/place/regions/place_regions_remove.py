import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.log.log import log
from Site.app.object.elem import elem
from Site.app.object.object import objectRemoveAt
from Site.models import Regions


@csrf_exempt
def place_regions_remove(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))
    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        _id = elem(_data, 'id')

        rList = Regions.objects.filter(Q(removeAt=None) & Q(pk=_id))
        objectRemoveAt(rList)
        log(request.user.pk, 'Настройки', 'Удаление', 'Регион', list(rList.values()))

        args['successText'] = 'Запись удалена'
    return HttpResponse(json.dumps(args, default=my_convert_datetime))

import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.log.log import log
from Site.app.object.elem import elem
from Site.models import Groups


@csrf_exempt
def group(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))
    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        _id = elem(_data, 'id')

        gList = Groups.objects.filter(Q(pk=_id))
        log(request.user.pk, 'Архив', 'Удаление', 'Сообщество', list(gList.values()))
        gList.delete()

        args['successText'] = 'Запись удалена'
    return HttpResponse(json.dumps(args, default=my_convert_datetime))

import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.log.log import log
from Site.app.object.elem import elem
from Site.controllers.control.analysis.success import success
from Site.models import ControlUser, GroupsCorrupt


@csrf_exempt
def reject(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))
    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        _id = elem(_data, 'id', None)
        _userId = elem(_data, 'userId', None)

        _user = ControlUser.objects.filter(Q(pk=_userId))

        if _user.exists():
            GroupsCorrupt.objects.filter(Q(pk=_id) & Q(groups__social__controlUser__in=_user)).delete()
            args.update(success(_user))
            log(request.user.pk, 'Данные КП', 'Управление', 'Удаление Сообщество')
        else:
            return HttpResponse(json.dumps({'warningText': 'Действие не выполнено'}, default=my_convert_datetime))
    return HttpResponse(json.dumps(args, default=my_convert_datetime))

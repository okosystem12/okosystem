import json
import os
import subprocess
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.db.read_files_for_bd import search_vk
from Site.app.log.log import log
from Site.app.object.elem import elem
from Site.app.status.setStatus import setStatus
from Site.models import ControlUser


@csrf_exempt
def search(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        id = elem(_data, 'id', None)

        controlUser = ControlUser.objects.filter(Q(pk=id)).first()
        if controlUser:
            setStatus(controlUser, 'search')

            log(request.user.pk, 'Данные КП', 'Управление', 'Поиск сотрудника')
            args = {
                'successText': 'Поиск сотрудника ' + controlUser.shortName(),
            }

            path_dir = os.path.abspath(os.path.join("database_vk"))
            search_vk(path_dir, controlUser)

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

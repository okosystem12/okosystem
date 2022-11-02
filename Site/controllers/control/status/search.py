import json
import os

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.db.read_files_for_bd import search_vk
from Site.app.object.elem import elem
from Site.app.status.setStatus import setStatus
from Site.models import ControlUser


@csrf_exempt
def search(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        id = elem(_data, 'id', None)

        controlUser = ControlUser.objects.filter(Q(pk=id)).first()
        if controlUser:
            setStatus(controlUser, 'search')

            args = {
                'successText': 'Поиск сотрудника ' + controlUser.shortName(),
            }


            path_dir = os.path.abspath(os.path.join("database_vk"))
            first_name = str(controlUser.firstNameT)
            last_name = str(controlUser.lastNameT)
            user = controlUser
            search_vk(path_dir, first_name, last_name, user)

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

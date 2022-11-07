import json
from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.db.read_files_for_bd import update_inf_users
from Site.models import LastUpdateConfig, Environments


@csrf_exempt
def update(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    if request.POST:
        LastUpdateConfig.objects.create(type='allUsersVK', dateStart=datetime.now())

        id_user_last = 0
        lastUserId = Environments.objects.filter(Q(key="lastUserId"))
        if lastUserId.exists():
            id_user_last = lastUserId.first().value

        update_inf_users(id_user_last=id_user_last)

    return HttpResponse(json.dumps({}, default=my_convert_datetime))

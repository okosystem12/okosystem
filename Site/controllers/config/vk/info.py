import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.models import LastUpdateConfig


@csrf_exempt
def info(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    args = {}
    if request.POST:
        allUsersVK = LastUpdateConfig.objects.filter(Q(type='allUsersVK')).order_by('-dateStart')
        if allUsersVK.exists():
            allUsersVK = allUsersVK.first().__dict__
        else:
            allUsersVK = None

        args = {
            'allUsersVK': allUsersVK
        }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

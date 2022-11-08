import json

from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime


@csrf_exempt
def auth_info(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'user': None}, default=my_convert_datetime))

    args = {'user': list(User.objects.filter(Q(pk=request.user.pk)).values())[0]}

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

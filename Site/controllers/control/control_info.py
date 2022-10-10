import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.models import ControlUser, ControlUserImg, File, Phone, Mail, Place
from Site.app.handler.place import placeObject


@csrf_exempt
def control_info(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    args = {}
    args.update(placeObject())

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

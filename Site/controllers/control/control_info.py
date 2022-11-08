import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.handler.placeObject import placeObject
from Site.models import Vch, Status


@csrf_exempt
def control_info(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    args = {}
    args.update({
        'vchList': list(Vch.objects.filter(Q(removeAt=None)).order_by('number').values()),
        'statusList': list(Status.objects.order_by('stage__value', 'value').values('id', 'name', 'stage__name'))
    })
    args.update(placeObject())

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.object.elem import elem
from Site.models import Vch


@csrf_exempt
def vch_get(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        _id = elem(_data, 'id', None)

        args = {
            'vch': list(Vch.objects.filter(Q(removeAt=None) & Q(pk=_id)).values()),
        }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))


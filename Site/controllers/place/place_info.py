import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.object.elem import elem
from Site.app.handler.place import placeObject


@csrf_exempt
def place_info(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    _data = json.loads(elem(request.POST, 'data', '{}'))
    _type = elem(_data, 'type')

    return HttpResponse(json.dumps(placeObject('regions'), default=my_convert_datetime))

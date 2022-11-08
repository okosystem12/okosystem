import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.object.elem import elem
from Site.models import File


@csrf_exempt
def control_work_img(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    img = elem(request.FILES, 'file')
    file = File.objects.create(
        name=img.name,
        file=img,
    )

    args = {
        'id': file.id,
        'name': file.name,
        'data': file.file.url,
    }
    return HttpResponse(json.dumps(args, default=my_convert_datetime))

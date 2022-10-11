import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.file.hardRemoveFile import hardRemoveFile
from Site.app.object.elem import elem
from Site.app.object.object import objectRemoveAt
from Site.models import ControlUserImg, ControlUser, File


@csrf_exempt
def control_work_img_remove(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        _id = elem(_data, 'id', [])
        _controlUserId = elem(_data, 'controlUserId', None)

        controlUser = ControlUser.objects.filter(Q(pk=_controlUserId)).first()

        if controlUser:
            objectRemoveAt(ControlUserImg.objects.filter(Q(file_id__in=_id)))
            objectRemoveAt(File.objects.filter(Q(removeAt=None) & Q(id__in=_id)))
        else:
            hardRemoveFile(_id)

        args['successText'] = 'Файл удалён'
        args['reload'] = True
    return HttpResponse(json.dumps(args, default=my_convert_datetime))

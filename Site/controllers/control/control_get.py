import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.handler.prepControlUserList import prepControlUserList
from Site.app.object.elem import elem
from Site.models import ControlUser, ControlUserImg, File, Phone, Mail, Place


@csrf_exempt
def control_get(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        _id = elem(_data, 'id', None)

        controlUserList = ControlUser.objects.filter(Q(removeAt=None) & Q(pk=_id))
        controlUserImgList = ControlUserImg.objects.filter(Q(removeAt=None) & Q(controlUser__in=controlUserList))
        fileList = File.objects.filter(Q(removeAt=None) & Q(controluserimg__in=controlUserImgList))
        phoneList = Phone.objects.filter(Q(removeAt=None) & Q(controlUser__in=controlUserList))
        mailList = Mail.objects.filter(Q(removeAt=None) & Q(controlUser__in=controlUserList))
        placeList = Place.objects.filter(
            Q(pk__in=controlUserList.values_list('birthPlace', flat=True))
            | Q(pk__in=controlUserList.values_list('livePlace', flat=True))
        )

        args = {
            'user': prepControlUserList(controlUserList),
            'fileList': list(fileList.values()),
            'controlUserImgList': list(controlUserImgList.values()),
            'controlUserList': list(controlUserList.values()),
            'phoneList': list(phoneList.values()),
            'mailList': list(mailList.values()),
            'placeList': list(placeList.values()),
        }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

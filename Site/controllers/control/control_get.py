import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.control.corruptionList import corruptionList
from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.object.elem import elem
from Site.app.table.control.value import value
from Site.models import ControlUser, ControlUserImg, File, Phone, Mail, Place, Social


@csrf_exempt
def control_get(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        _id = elem(_data, 'id', None)
        _full = elem(_data, 'full', None)

        controlUserList = ControlUser.objects.filter(Q(removeAt=None) & Q(pk=_id))
        controlUserImgList = ControlUserImg.objects.filter(Q(removeAt=None) & Q(controlUser__in=controlUserList))
        fileList = File.objects.filter(Q(removeAt=None) & Q(controluserimg__in=controlUserImgList))
        phoneList = Phone.objects.filter(Q(removeAt=None) & Q(controlUser__in=controlUserList))
        mailList = Mail.objects.filter(Q(removeAt=None) & Q(controlUser__in=controlUserList))
        placeList = Place.objects.filter(
            Q(pk__in=controlUserList.values_list('birthPlace', flat=True))
            | Q(pk__in=controlUserList.values_list('livePlace', flat=True))
        )

        if _full:
            socialList = Social.objects.filter(Q(controlUser__in=controlUserList)).values()
            cList = corruptionList(controlUserList)
        else:
            socialList = []
            cList = []

        args = {
            'controlUser': value(controlUserList),
            'fileList': list(fileList.values()),
            'controlUserImgList': list(controlUserImgList.values()),
            'controlUserList': list(controlUserList.values()),
            'phoneList': list(phoneList.values()),
            'mailList': list(mailList.values()),
            'placeList': list(placeList.values()),
            'socialList': list(socialList),
            'corruptList': cList
        }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

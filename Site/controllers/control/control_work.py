import json
from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.log.log import log
from Site.app.object.elem import elem
from Site.app.object.objDate import objDate
from Site.app.object.object import objectRemoveAt
from Site.app.object.objectUpdate import objectUpdate
from Site.app.status.setStatus import setStatus
from Site.models import ControlUser, Place, ControlUserImg, Phone, Mail, File


@csrf_exempt
def control_work(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout': True}, default=my_convert_datetime))

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        id = elem(_data, 'id', None)
        _old = None
        _new = False
        controlUser = ControlUser.objects.filter(Q(pk=id)).first()
        if not controlUser:
            _new = True
            controlUser = ControlUser.objects.create()
            setStatus(controlUser)
        else:
            _old = controlUser

        birthDate = objDate(_data, 'birthDate', '0.0.0').split('.')

        controlUser.lastName = elem(_data, 'lastName')
        controlUser.firstName = elem(_data, 'firstName')
        controlUser.patronymic = elem(_data, 'patronymic')
        controlUser.lastNameT = elem(_data, 'lastNameT')
        controlUser.firstNameT = elem(_data, 'firstNameT')
        controlUser.patronymicT = elem(_data, 'patronymicT')
        controlUser.birthDay = birthDate[0]
        controlUser.birthMonth = birthDate[1]
        controlUser.birthYear = birthDate[2]
        controlUser.schools = elem(_data, 'schools')
        controlUser.universities = elem(_data, 'universities')
        controlUser.work = elem(_data, 'work')
        controlUser.vch_id = elem(_data, 'vch')
        controlUser.updatedAt = datetime.now()

        birthCountry = elem(_data, 'birthCountry')
        birthRegion = elem(_data, 'birthRegion')
        birthCity = elem(_data, 'birthCity')

        if birthCountry or birthRegion or birthCity:
            birthPlace = Place.objects.create(country_id=birthCountry, region_id=birthRegion, city_id=birthCity, )
            controlUser.birthPlace = birthPlace

        liveCountry = elem(_data, 'liveCountry')
        liveRegion = elem(_data, 'liveRegion')
        liveCity = elem(_data, 'liveCity')

        if liveCountry or liveRegion or liveCity:
            livePlace = Place.objects.create(country_id=liveCountry, region_id=liveRegion, city_id=liveCity, )
            controlUser.livePlace = livePlace
        controlUser.save()

        for f in File.objects.filter(Q(removeAt=None) & Q(pk__in=elem(_data, 'photoList', []))).iterator():
            if not ControlUserImg.objects.filter(Q(file=f)).exists():
                ControlUserImg.objects.create(controlUser=controlUser, file=f)

        userPhoneList = Phone.objects.filter(Q(controlUser=controlUser))
        objectRemoveAt(userPhoneList.exclude(Q(id__in=elem(_data, 'phoneIdList', []))))
        objectUpdate(Phone, elem(_data, 'phoneList', []), controlUser)

        userMailList = Mail.objects.filter(Q(controlUser=controlUser))
        objectRemoveAt(userMailList.exclude(Q(id__in=elem(_data, 'mailIdList', []))))
        objectUpdate(Mail, elem(_data, 'mailList', []), controlUser)

        if _new:
            log(request.user.pk, 'Данные КП', 'Создание', '')
        else:
            if _old:
                log(request.user.pk, 'Данные КП', 'Изменение', '', {'old': _old.fullName()})

        args = {'successText': 'Запись добавлена' if not _new else 'Запись обновлена', }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

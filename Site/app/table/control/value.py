from django.db.models import Q

from Site.app.datetime.bDate import bDate
from Site.app.handler.placeDisassemble import placeDisassemble
from Site.app.handler.prepSocial import prepSocial
from Site.app.handler.prepStatus import prepStatus
from Site.app.handler.vchNumber import vchNumber
from Site.models import Phone, Mail


def value(oList):
    result = []

    for user in oList:
        cur = {}
        cur.update(user.__dict__)
        cur.update({
            'fullName': user.fullName(),
            'shortName': user.shortName,
            'birthDate': bDate(user.birthDay, user.birthMonth, user.birthYear),
            'phoneList': list(Phone.objects.filter(Q(controlUser=user)).values()),
            'mailList': list(Mail.objects.filter(Q(controlUser=user)).values()),
            'birthPlace': placeDisassemble(user.birthPlace),
            'livePlace': placeDisassemble(user.livePlace),
            'vch': vchNumber(user.vch_id),
            'status': prepStatus(user.status_id),
            'control': user.pk,
            'socialsList': prepSocial(user),
        })

        result.append(cur)

    return result

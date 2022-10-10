from django.db.models import Q

from Site.app.datetime.bDate import bDate
from Site.app.handler.placeDisassemble import placeDisassemble
from Site.models import Phone, Mail


def prepControlUserList(controlUserList):
    result = []

    for user in controlUserList:

        cur = {}
        cur.update(user.__dict__)
        cur.update({
            'fullName': user.fullName(),
            'shortName': user.shortName(),
            'birthDate':  bDate(user.birthDay, user.birthMonth, user.birthYear),
            'phoneList': list(Phone.objects.filter(Q(controlUser=user)).values()),
            'mailList': list(Mail.objects.filter(Q(controlUser=user)).values()),
            'birthPlace': placeDisassemble(user.birthPlace),
            'livePlace': placeDisassemble(user.livePlace),
        })

        result.append(cur)

    return result

from threading import Thread

from django.db.models import Q

from Site.app.extend.action import action
from Site.app.text.alter.alterPart import alterPart
from Site.app.text.decim.decimPart import decimPart
from Site.app.text.inflect import inflect
from Site.app.text.mimic.mimicPart import mimicPart
from Site.app.text.translit.translitPart import translitPart
from Site.models import CorruptExtend, CorruptInfo


def extend(_id):
    Thread(target=extend_t, args=[_id]).start()  # extend_t(_id)


def extend_t(_id):
    _corrupt = CorruptInfo.objects.filter(Q(pk=_id)).first()

    a_list = [inflect, decimPart, mimicPart, alterPart, translitPart]

    if _corrupt:
        _corrupt.extend_finish = len(a_list) + 1
        _corrupt.save()

        for a in a_list:
            action(_corrupt.pk, a)

from django.db.models import Q

from Site.models import CorruptExtendFin


def value(oList):
    result = []

    for o in oList:
        extend = CorruptExtendFin.objects.filter(Q(corruptInfo_id=o.id))

        extend_finish = (extend.count() / (o.extend_finish if o.extend_finish != 0 else 100)) * 100

        result.append(
            {'id': o.id, 'value': o.value, 'info': o.info, 'extend_count': sum(extend.values_list('count', flat=True)),
             'extend_finish': {'title': "Подготовка словаря" if extend_finish != 100 else "Словарь готов к работе",
                               'value': extend_finish, 'color': '#0075ff' if extend_finish != 100 else "#5cb85c"}, })

    return result

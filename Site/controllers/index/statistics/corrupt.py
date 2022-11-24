import json

from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.models import CorruptInfo, CorruptExtendFin


@csrf_exempt
def corrupt(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout': True}, default=my_convert_datetime))

    args = {}
    if request.POST:
        corruptList = []

        corruptClear = CorruptInfo.objects.filter(Q(removeAt=None) & Q(tech=False))
        corruptDict = CorruptExtendFin.objects.filter(Q(corruptInfo__in=corruptClear)).values_list('count', flat=True)

        corruptList.append(
            {'title': 'Всего', 'value': corruptClear.count(),
             'subList': [{'title': 'Словарь',
                          'value': sum(corruptDict)}]})

        args = {'corruptList': corruptList}

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

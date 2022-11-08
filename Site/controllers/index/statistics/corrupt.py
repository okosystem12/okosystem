import json

from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.models import CorruptInfo


@csrf_exempt
def corrupt(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    args = {}
    if request.POST:
        corruptList = []

        corruptClear = CorruptInfo.objects.filter(Q(removeAt=None) & Q(tech=False))

        corruptList.append({
            'title': 'Всего',
            'value': corruptClear.count()
        })

        args = {
            'corruptList': corruptList
        }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

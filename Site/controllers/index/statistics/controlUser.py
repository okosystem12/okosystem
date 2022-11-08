import json

from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.models import ControlUser, StatusStage, Status


@csrf_exempt
def controlUser(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    args = {}
    if request.POST:
        controlUserList = []

        controlUserClear = ControlUser.objects.filter(Q(removeAt=None))

        controlUserList.append({
            'title': 'Всего',
            'value': controlUserClear.count()
        })

        for stage in StatusStage.objects.order_by('value'):
            subList = []
            for status in Status.objects.filter(Q(stage=stage)):
                danger = False
                value = controlUserClear.filter(Q(status=status)).count()


                subList.append({
                    'title': status.name,
                    'value': value
                })

            if len(subList):
                controlUserList.append({'title': stage.name, 'subList': subList})

        args = {
            'controlUserList': controlUserList
        }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

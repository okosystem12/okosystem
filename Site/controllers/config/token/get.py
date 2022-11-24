import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.models import TokenAdmin


@csrf_exempt
def get(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    args = {}
    if request.POST:
        tokenVK = TokenAdmin.objects.first()
        if tokenVK:
            args = {
                'tokenVK': tokenVK.tokenVK,
            }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

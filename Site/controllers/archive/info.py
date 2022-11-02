import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.models import ControlUser, CorruptInfo


@csrf_exempt
def info(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    usersList = ControlUser.objects.filter(
        Q(social__post__postcorrupt__isnull=False) | Q(social__groups__groupscorrupt__isnull=False) | Q(
            social__video__videocorrupt__isnull=False) | Q(social__inf__infcorrupt__isnull=False) | Q(
            social__photos__photoscorrupt__isnull=False))

    args = {'usersList': list(ControlUser.objects.filter(Q(pk__in=usersList)).values()),
        'corruptInfoList': list(CorruptInfo.objects.all().values())}

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

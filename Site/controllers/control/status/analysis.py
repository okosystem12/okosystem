import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.analysis.init import init
from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.object.elem import elem
from Site.app.status.setStatus import setStatus
from Site.app.status.updateByAnalysis import updateByAnalysis
from Site.app.status.updateBySocial import updateBySocial
from Site.models import ControlUser


@csrf_exempt
def analysis(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        id = elem(_data, 'id', None)

        controlUser = ControlUser.objects.filter(Q(pk=id)).first()
        if controlUser:
            updateByAnalysis(controlUser)
            init(controlUser)

            args = {
                'successText': 'Анализ сотрудника ' + controlUser.shortName(),
            }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.object.elem import elem
from Site.models import Regions, Countries


@csrf_exempt
def get(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        _id = elem(_data, 'id', None)

        countriesList = Countries.objects.filter(Q(removeAt=None))
        args = {
            'region': list(
                Regions.objects.filter(Q(removeAt=None) & Q(pk=_id) & Q(country__in=countriesList)).values()),
        }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

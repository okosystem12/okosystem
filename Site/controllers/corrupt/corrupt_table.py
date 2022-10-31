import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.table.corrupt.order import order
from Site.app.table.corrupt.search import search
from Site.app.table.corrupt.value import value
from Site.app.table.data import data
from Site.models import CorruptInfo


@csrf_exempt
def corrupt_table(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    args = data(request, CorruptInfo.objects.filter(Q(tech=False)), search, order,  value)
    # args = data(request, CorruptInfo.objects.filter(Q(byAdmin=False)), search, order,  value)

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

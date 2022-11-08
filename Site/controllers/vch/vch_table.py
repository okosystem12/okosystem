import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.table.data import data
from Site.app.table.vch.order import order
from Site.app.table.vch.search import search
from Site.app.table.vch.value import value
from Site.app.table.vch.filter import filter
from Site.models import Vch


@csrf_exempt
def vch_table(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))

    args = data(request, Vch.objects, search, order, value, filter)

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.table.control.order import order
from Site.app.table.control.search import search
from Site.app.table.control.value import value
from Site.app.table.data import data
from Site.models import ControlUser


@csrf_exempt
def control_table(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    args = data(request.POST, ControlUser, search, order, value)

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

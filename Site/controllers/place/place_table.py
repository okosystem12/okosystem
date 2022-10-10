import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.handler.orderControlUserList import orderControlUserList
from Site.app.handler.prepControlUserList import prepControlUserList
from Site.app.handler.tableConfig import tableConfig
from Site.models import Countries, Regions, Cities


@csrf_exempt
def place_table(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    tc = tableConfig(request.POST)

    countriesList = Countries.objects.filter(Q(removeAt=None))
    regionsList = Regions.objects.filter(Q(removeAt=None))
    citiesList = Cities.objects.filter(Q(removeAt=None))



    iTotalRecords = controlUserList.count()

    if tc['search'] != '':
        for word in tc['search'].split(' '):
            controlUserList = controlUserList.filter(

            )

    iTotalDisplayRecords = controlUserList.count()

    controlUserList = orderControlUserList(controlUserList, tc['column_list'][tc['order']], tc['order_dir'])

    controlUserList = controlUserList[tc['start']:(tc['length'] + tc['start'])]

    args = {
        "draw": tc['draw'],
        "iTotalRecords": iTotalRecords,
        "iTotalDisplayRecords": iTotalDisplayRecords,
        'data': prepControlUserList(controlUserList),
    }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

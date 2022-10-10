import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.handler.tableConfig import tableConfig
from Site.models import Vch


@csrf_exempt
def vch_table(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    tc = tableConfig(request.POST)

    vchList = Vch.objects.filter(Q(removeAt=None))

    iTotalRecords = vchList.count()

    if tc['search'] != '':
        for word in tc['search'].split(' '):
            vchList = vchList.filter(
                Q(number__icontains=word)
            )

    iTotalDisplayRecords = vchList.count()

    if tc['column_list'][tc['order']] == 'number':
        vchList = vchList.order_by(
            tc['order_dir'] + 'number'
        )

    vchList = vchList[tc['start']:(tc['length'] + tc['start'])]

    args = {
        "draw": tc['draw'],
        "iTotalRecords": iTotalRecords,
        "iTotalDisplayRecords": iTotalDisplayRecords,
        'data': list(vchList.values()),
    }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

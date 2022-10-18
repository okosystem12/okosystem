import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.handler.orderControlUserList import orderControlUserList
from Site.app.handler.prepControlUserList import prepControlUserList
from Site.app.table.tableConfig import tableConfig
from Site.models import ControlUser


@csrf_exempt
def control_table(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    tc = tableConfig(request.POST)

    controlUserList = ControlUser.objects.filter(Q(removeAt=None))

    iTotalRecords = controlUserList.count()

    if tc['search'] != '':
        for word in tc['search'].split(' '):
            controlUserList = controlUserList.filter(
                Q(lastName__icontains=word)
                | Q(firstName__icontains=word)
                | Q(patronymic__icontains=word)
                | Q(updatedAt__icontains=word)
                | Q(birthDay__icontains=word)
                | Q(birthMonth__icontains=word)
                | Q(birthYear__icontains=word)
                | Q(phone__value__icontains=word)
                | Q(mail__value__icontains=word)
                | Q(birthPlace__country__title__icontains=word)
                | Q(birthPlace__region__title__icontains=word)
                | Q(birthPlace__city__title__icontains=word)
                | Q(livePlace__country__title__icontains=word)
                | Q(livePlace__region__title__icontains=word)
                | Q(livePlace__city__title__icontains=word)
                | Q(schools__icontains=word)
                | Q(universities__icontains=word)
                | Q(work__icontains=word)
                | Q(vch__number__icontains=word)
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

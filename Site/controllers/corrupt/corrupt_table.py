import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.table.tableConfig import tableConfig
from Site.models import CorruptInfo


@csrf_exempt
def corrupt_table(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    tc = tableConfig(request.POST)

    corruptList = CorruptInfo.objects.filter(Q(removeAt=None))

    iTotalRecords = corruptList.count()

    if tc['search'] != '':
        for word in tc['search'].split(' '):
            corruptList = corruptList.filter(
                Q(value__icontains=word)
                | Q(info__icontains=word)
            )

    iTotalDisplayRecords = corruptList.count()

    if tc['column_list'][tc['order']] == 'value':
        corruptList = corruptList.order_by(
            tc['order_dir'] + 'value'
        )
    elif tc['column_list'][tc['order']] == 'info':
        corruptList = corruptList.order_by(
            tc['order_dir'] + 'info'
        )

    corruptList = corruptList[tc['start']:(tc['length'] + tc['start'])]

    args = {
        "draw": tc['draw'],
        "iTotalRecords": iTotalRecords,
        "iTotalDisplayRecords": iTotalDisplayRecords,
        'data': list(corruptList.values()),
    }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.object.elem import elem
from Site.models import Column, Render, PatternColumn, PatternTable


@csrf_exempt
def table_info(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')

    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        table = elem(_data, 'table')

        columnsList = Column.objects.filter(Q(table__type=table)).order_by('-fixed', 'order', 'pk')

        if columnsList.count() != 0:
            renderList = Render.objects.filter(Q(column__in=columnsList))
            patternList = PatternTable.objects.filter(Q(table__type=table))
            patternColumnsList = PatternColumn.objects.filter(Q(pattern__in=patternList))

            args = {
                'columnsList': list(columnsList.values()),
                'renderList': list(renderList.values()),
                'patternList': list(patternList.values()),
                'patternColumnsList': list(patternColumnsList.values()),
            }

    return HttpResponse(json.dumps(args, default=my_convert_datetime))

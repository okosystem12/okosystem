import json

from django.db.models import Q

from Site.app.object.elem import elem
from Site.app.table.tableConfig import tableConfig


def data(_request, _object, search, order, value, filter):
    tc = tableConfig(_request.POST)

    oList = _object.filter(Q(removeAt=None))

    iTotalRecords = oList.count()

    _data = json.loads(elem(_request.GET, 'data', '{}'))

    oList = filter(oList, _data)

    if tc['search'] != '':
        oList = search(oList, tc['search'])

    iTotalDisplayRecords = oList.count()

    oList = order(oList, tc['column_list'][tc['order']], tc['order_dir'])

    oList = oList[tc['start']:(tc['length'] + tc['start'])]
    
    return {
        "draw": tc['draw'],
        "iTotalRecords": iTotalRecords,
        "iTotalDisplayRecords": iTotalDisplayRecords,
        'data': value(oList),
    }

from django.db.models import Q

from Site.app.table.tableConfig import tableConfig


def data(_post, _object, search, order):
    tc = tableConfig(_post)

    oList = _object.objects.filter(Q(removeAt=None))

    iTotalRecords = oList.count()

    if tc['search'] != '':
        for word in tc['search'].split(' '):
            oList = search(oList, word)

    iTotalDisplayRecords = oList.count()

    oList = order(oList, tc['column_list'][tc['order']], tc['order_dir'])

    oList = oList[tc['start']:(tc['length'] + tc['start'])]
    
    return {
        "draw": tc['draw'],
        "iTotalRecords": iTotalRecords,
        "iTotalDisplayRecords": iTotalDisplayRecords,
        'data': list(oList.values()),
    }

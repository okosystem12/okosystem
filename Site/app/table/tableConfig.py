from Site.app.object.elem import elem


def tableConfig(request):
    
    draw = int(elem(request, 'draw', 0))
    length = int(elem(request, 'length', 0))
    order = int(elem(request, 'order[0][column]', 0))
    order_dir = elem(request, 'order[0][dir]', 'asc')

    order_dir = '' if order_dir == 'asc' else '-'

    search = elem(request, 'search[value]')

    start = int(elem(request, 'start', 0))

    column_list = []

    key = 0
    while True:
        data = elem(request, 'columns[' + str(key) + '][data]', None)
        if data:
            column_list.append(data)
            key += 1
        else:
            break
    return {
        'draw': draw,
        'length': length,
        'order': order,
        'order_dir': order_dir,
        'search': search,
        'start': start,
        'column_list': column_list,
    }

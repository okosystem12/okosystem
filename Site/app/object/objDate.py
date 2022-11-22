from Site.app.object.elem import elem


def objDate(obj, key, default='T'):
    return elem(obj, key, default).split('T')[0]

from django.db.models import Q

from Site.app.object.elem import elem


def objectUpdate(obj, listVal, controlUser):
    for val in listVal:
        o = obj.objects.filter(Q(id=elem(val, 'id'))).first()
        if not o:
            o = obj.objects.create()
        o.value = elem(val, 'value', '')
        o.controlUser = controlUser
        o.save()

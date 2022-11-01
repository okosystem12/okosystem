import json
from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.object.elem import elem
from Site.app.social.unsetSocial import unsetSocial
from Site.app.status.setStatus import setStatus
from Site.app.status.updateBySocial import updateBySocial
from Site.controllers.control.social.success import success
from Site.models import Social, ControlUser


@csrf_exempt
def reject(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        _id = elem(_data, 'id', None)
        _userId = elem(_data, 'userId', None)

        _controlUser = ControlUser.objects.filter(Q(pk=_userId))

        if _controlUser.exists():
            _user = _controlUser.first()
            _social = Social.objects.filter(Q(pk=_id)).first()
            if _social:
                if _social.confirmedAt:
                    args.update({'reloadTable': True})
                _social.delete()

            args.update(success(_controlUser))
        else:
            return HttpResponse(json.dumps({'warningText': 'Действие не выполнено'}, default=my_convert_datetime))
    return HttpResponse(json.dumps(args, default=my_convert_datetime))

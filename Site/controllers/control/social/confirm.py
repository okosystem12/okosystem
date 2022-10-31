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
from Site.models import Social, ControlUser


@csrf_exempt
def confirm(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        _id = elem(_data, 'id', None)
        _userId = elem(_data, 'userId', None)

        _user = ControlUser.objects.filter(Q(pk=_userId)).first()

        if _user:
            _social = Social.objects.filter(Q(pk=_id)).first()
            if _social:
                _social.confirmedAt = datetime.now()
                _social.save()
                args.update({'reloadTable': True})
                unsetSocial(_user, _social.value)
                args.update({
                    'closeModal': updateBySocial(_user),
                    'successText': 'Действие выполнено'
                })
        else:
            return HttpResponse(json.dumps({'warningText': 'Действие не выполнено'}, default=my_convert_datetime))
    return HttpResponse(json.dumps(args, default=my_convert_datetime))

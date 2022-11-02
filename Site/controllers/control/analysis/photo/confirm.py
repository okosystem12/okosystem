import json
from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.object.elem import elem
from Site.controllers.control.analysis.success import success
from Site.models import ControlUser, PhotosCorrupt


@csrf_exempt
def confirm(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    args = {}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        _id = elem(_data, 'id', None)
        _userId = elem(_data, 'userId', None)

        _user = ControlUser.objects.filter(Q(pk=_userId))

        if _user.exists():
            _c = PhotosCorrupt.objects.filter(Q(pk=_id) & Q(photo__social__controlUser__in=_user)).first()
            if _c:
                _c.confirmedAt = datetime.now()
                _c.save()

                args.update(success(_user))
        else:
            return HttpResponse(json.dumps({'warningText': 'Действие не выполнено'}, default=my_convert_datetime))
    return HttpResponse(json.dumps(args, default=my_convert_datetime))

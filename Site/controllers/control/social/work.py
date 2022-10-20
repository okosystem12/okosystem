import json
from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.object.elem import elem
from Site.app.status.setStatus import setStatus
from Site.models import Social, ControlUser


@csrf_exempt
def work(request):
    if request.user.pk is None:
        return render(request, 'Site/login.html')
    args = {'closeModal': False}
    if request.POST:
        _data = json.loads(elem(request.POST, 'data', '{}'))
        _id = elem(_data, 'id', None)
        _action = elem(_data, 'action', None)
        _userId = elem(_data, 'userId', None)
        _value = elem(_data, 'value')

        _social = Social.objects.filter(Q(pk=_id)).first()
        _user = ControlUser.objects.filter(Q(pk=_userId)).first()

        print(_action)
        print(_value)
        if _user:
            if not _social:
                if _action == 'add':
                    _social = Social.objects.create(
                        controlUser=_user,
                        value=_value,
                        confirmedAt=datetime.now()
                    )
                    args.update({'social': _social.__dict__, 'successText': 'Действие выполнено'})
            else:
                if _action == 'reject':
                    if _social.confirmedAt:
                        args.update({'reloadTable': True})
                    _social.delete()

                if _action == 'confirm':
                    _social.confirmedAt = datetime.now()
                    _social.save()
                    args.update({'reloadTable': True})

                _social_list = Social.objects.filter(Q(controlUser=_user))
                if _social_list.count() == 0:
                    setStatus(_user)
                    args.update({'closeModal': True})

                if _social_list.filter(Q(confirmedAt__isnull=True)).count() == 0:
                    setStatus(_user, 'work')
                    args.update({'closeModal': True})

                args.update({'successText': 'Действие выполнено'})
        else:
            args.update({'warningText': 'Действие не выполнено'})
    return HttpResponse(json.dumps(args, default=my_convert_datetime))

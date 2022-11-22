import json
from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Site.app.datetime.my_convert_datetime import my_convert_datetime
from Site.app.log.log import log
from Site.app.object.elem import elem
from Site.app.social.unsetSocial import unsetSocial
from Site.app.status.setStatus import setStatus
from Site.app.status.updateBySocial import updateBySocial
from Site.controllers.control.social.success import success
from Site.models import Social, ControlUser, Post, Video, Photos, Inf, Groups, PostCorrupt, VideoCorrupt, PhotosCorrupt, \
    InfCorrupt, GroupsCorrupt, PostsChecks, VideoChecks, PhotosChecks, GroupsChecks


@csrf_exempt
def reject(request):
    if request.user.pk is None:
        return HttpResponse(json.dumps({'logout':True}, default=my_convert_datetime))
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

                Post.objects.filter(Q(social=_social)).delete()
                Video.objects.filter(Q(social=_social)).delete()
                Photos.objects.filter(Q(social=_social)).delete()
                Inf.objects.filter(Q(social=_social)).delete()
                Groups.objects.filter(Q(social=_social)).delete()

                PostsChecks.objects.filter(Q(social=_social)).delete()
                VideoChecks.objects.filter(Q(social=_social)).delete()
                PhotosChecks.objects.filter(Q(social=_social)).delete()
                GroupsChecks.objects.filter(Q(social=_social)).delete()

                PostCorrupt.objects.filter(Q(post__social=_social)).delete()
                VideoCorrupt.objects.filter(Q(video__social=_social)).delete()
                PhotosCorrupt.objects.filter(Q(photo__social=_social)).delete()
                InfCorrupt.objects.filter(Q(inf__social=_social)).delete()
                GroupsCorrupt.objects.filter(Q(groups__social=_social)).delete()

                _social.delete()

                log(request.user.pk, 'Данные ЛС', 'Управление', 'Удаление соц. сети')
            args.update(success(_controlUser))
        else:
            return HttpResponse(json.dumps({'warningText': 'Действие не выполнено'}, default=my_convert_datetime))
    return HttpResponse(json.dumps(args, default=my_convert_datetime))

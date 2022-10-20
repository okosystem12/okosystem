from threading import Thread

from django.db.models import Q

from Site.app.status.setStatus import setStatus
from Site.models import Social
from genering_profils_vk.src.func import *


def init(user=None):
    Thread(target=initT, args=[user]).start()


def initT(user=None):
    if user:
        socialList = Social.objects.filter(Q(controlUser=user))
        for one in socialList:
            print("start")

            search_post_vk_id(one.value)
            # search_name_groups_vk_id(one.value)
            # search_name_videos_vk_id(one.value)
            # search_inf_users_vk_id(one.value)
            # downloading_search_photos(one.value)

        else:
            print('NO initT')
        setStatus(user, 'warning' if socialList.count() else 'success')
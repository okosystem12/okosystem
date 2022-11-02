from threading import Thread

from django.db.models import Q

from Site.app.status.setStatus import setStatus
from Site.models import Social, CorruptInfo
from genering_profils_vk.src.func import *
def init(user=None):
    Thread(target=initT, args=[user]).start()
    # update_inf_users(756000000, list_token=config.list_token)
    # delete()
    # add_token_apps()


    # word_list = list(CorruptInfo.objects.all().values())
    pass

def initT(user=None):
    if user:
        socialList = Social.objects.filter(Q(controlUser=user))
        for one in socialList.iterator():
            print("start")

            # search_post_vk_id(one.value)
            # search_name_groups_vk_id(one.value)
            # search_name_videos_vk_id(one.value)
            # search_inf_users_vk_id(one.value)
            # downloading_search_photos(one.value)

        else:
            print('NO initT')
        setStatus(user, 'warning' if socialList.exists() else 'success')
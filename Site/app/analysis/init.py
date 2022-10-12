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
            abs_dir_path = r"D:\oko\okosystem\genering_profils_vk\verification_result"
            abs_dir_path_user = os.path.join(abs_dir_path, str(one.value))
            search_post_vk_id(one.value, abs_dir_path_user)
            search_name_groups_vk_id(one.value, abs_dir_path_user)
            search_name_videos_vk_id(one.value, abs_dir_path_user)
            search_inf_users_vk_id(one.value, abs_dir_path_user)
        print('initT')
        setStatus(user, 'warning' if socialList.count() else 'success')

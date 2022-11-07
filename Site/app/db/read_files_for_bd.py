import os
from datetime import datetime

from django.db.models import Q

from Site.app.status.updateBySocial import updateBySocial

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django

django.setup()

import asyncio

from time import time

import nest_asyncio
from aiohttp import ClientSession

from genering_profils_vk.src import config
import json

from Site.models import AllUsersVK, Environments, Social, ControlUser, LastUpdateConfig

list_data = []


def search_vk(path_dir, user):
    # AllUsersVK.objects.all().delete()
    # return
    print("Зашли в функцию")
    for namefile in os.listdir(path_dir):
        print("Зашли в каталог")
        with open(os.path.join(path_dir, namefile), "r", encoding="utf-8") as file:
            print("Открыли файл", os.path.join(path_dir, namefile))
            data = [json.loads(line) for line in file]

        data_update = [elem for l in data for elem in l if
                       elem.get("deactivated") not in ("deleted", "banned") and not elem.get("is_closed")]
        print("Сформировали обновленный список пользователей")
        for l in data_update:
            if l.get("first_name", "") == user.firstNameT and l.get("last_name", "") == user.lastNameT:
                print("Нашли совпаление с id", l.get("id", ""))
                if not Social.objects.filter(Q(controlUser=user) & Q(value=l.get("id", ""))).exists():
                    Social.objects.create(controlUser=user,
                                          value=l.get("id", ""))

        data.clear()
        data_update.clear()
        updateBySocial(user, 'robot')


# обновление базы пользователей
# lastUserId = Environments.objects.filter(key="lastUserId").first()
# id_user_last = lastUserId.value
def update_inf_users(id_user_last, list_token=config.list_token):
    max_id = -1
    nest_asyncio.apply()

    async def bound_fetch_zero(sem, id, session):
        async with sem:
            await fetch_zero(id, session)

    async def fetch_zero(id, session):
        url = build_url(id)
        try:
            async with session.get(url) as response:
                # Считываем json
                resp = await response.text()
                js = json.loads(resp)
                for it in range(25):
                    list_data.append(js["response"][it][0])

        except Exception as ex:
            print(resp)
            return

    def build_url(id):
        api = "API.users.get({{'user_ids':{},'fields':'deactivated, is_closed, first_name, last_name, bdate, city, home_town'}})".format(
            id * 25 + 1)
        for i in range(2, 26):
            api += ",API.users.get({{'user_ids':{},'fields':'deactivated, is_closed, first_name, last_name, bdate, city, home_town'}})".format(
                id * 25 + i)
        url = 'https://api.vk.com/method/execute?access_token={}&v=5.101&code=return%20[{}];'.format(
            list_token[id % len(list_token)], api)
        return url

    async def run_zero(id):
        tasks = []
        sem = asyncio.Semaphore(1000)

        async with ClientSession() as session:
            #  Значение 3200 зависит от вашего числа токенов
            param3200 = 320
            for id in range((id - 1) * param3200, id * param3200):
                task = asyncio.ensure_future(bound_fetch_zero(sem, id, session))
                tasks.append(task)

            responses = asyncio.gather(*tasks)
            await responses
            del responses
            await session.close()

    # Запускаем  сборщик
    # threshold = 17
    # param_count = 554
    st = time()
    # 105 and 900
    all = 320 * 25 * 900
    threshold = id_user_last // all
    for i in range(threshold, threshold + 1):
        param_count = 900
        for query in range(i * param_count + 1, (i + 1) * param_count + 1):
            try:
                data_update = [elem for elem in list_data if
                               elem.get("deactivated") not in ("deleted", "banned") and not elem.get("is_closed")]
                for l in data_update:
                    max_id = int(l.get("id"))
                    print(max_id)
                    string = json.dumps(data_update)
                    with open(os.path.abspath(
                            os.path.join("..", "..", "..", "database_vk", f"update_database-VK-users_{query}.txt")),
                              "a", encoding="utf-8") \
                            as file:
                        file.write(string + "\n")

                list_data.clear()
                data_update.clear()
                print(query, time() - st)
                st = time()
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(run_zero(query))
            except Exception as e:
                print(e)
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(run_zero(query))

    # запись в базу максимального id
    lastUserId = Environments.objects.filter(key="lastUserId")
    if not lastUserId.exists():
        lastUserId = Environments.objects.create(key="lastUserId")
    lastUserId.value = str(max_id)
    lastUserId.save()

    lastUC = LastUpdateConfig.objects.filter(Q(type='allUsersVK') & Q(type='allUsersVK'))
    if lastUC.exists():
        lastUC.update(dateEnd=datetime.now())


# lastUserId = Environments.objects.filter(key="lastUserId").first()
# id_user_last = int(lastUserId.value)
#
# database_vk_path_dir = r"C:\Users\user.303-ARM2\PycharmProjects\okosystem\genering_profils_vk\database_vk"
# update_inf_users(id_user_last=id_user_last)

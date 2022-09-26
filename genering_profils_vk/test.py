import vk_api

import json
import requests

from time import time
from pprint import pprint

# чтение файла токенов (путь до файла -> список токенов)
def read_tokens_file(file):
    list_token = []
    with open(file, 'r') as f:
        for line in f:
            list_token.append(str(line).rstrip('\n'))
    return list_token




# Генерация url к апи вк, 25 запросов в одном (номер токена в списке, список токенов -> ссылка-запрос)
def build_url(id, list_token):
    api = "API.users.get({{'user_ids':{},'fields':'deactivated, is_closed, first_name, last_name, bdate, city, home_town'}})".format(
        id * 25 + 1)
    for i in range(2, 26):
        api += ",API.users.get({{'user_ids':{},'fields':'deactivated, is_closed, first_name, last_name, bdate, city, home_town'}})".format(
            id * 25 + i)
    url = "https://api.vk.com/method/execute?access_token={}&v=5.101&code=return%20[{}];".format(
        list_token[id%len(list_token)], api)
    return url





def fetch_zero(url, vk):
    list_data = []

    try:
         with requests.get(url) as response:
                # Считываем json
                resp = response.text
                js = json.loads(resp)
                list_users = [x for x in js['response'] if x != False]
                # --------------------------- тут основной запрос по базе ---------------------------------------------
                for it in list_users:
                    try:
                        #if it[0]['city']['id'] == 2:
                            list_data.append(it[0]['id'])
                    except Exception:
                        pass

                # -----------------------------------------------------------------------------------------------------
    except Exception:
        pass
    return list_data

def genering_id(i, list_token, vk, list_data):
    url = build_url(i, list_token)
    list_data.extend(fetch_zero(url, vk))







session = vk_api.VkApi(token="vk1.a.R7kz0YtsBIdvSC_81mtiijWqzJSXlbg9lIlPFkSwnuOh81j_hkZtS3oPZoNB4a0YNw8d4dv7XslhVI_jMxkYmUnNnMgcdldvOrDMqCTnrMAHUPJTL_tk2GmF5hxwr3RXYIRMunQFZxaRGepHpO33qkRYh4ZK9i7J9-HKNJ8ScKAZWb1C7e_J5M7RICsDPeyY")
vk = session.get_api()

list_token = read_tokens_file("tokens/list_tokens.txt")
list_data = []

start = time()
for i in range(10):
    genering_id(i, list_token, vk, list_data)
print(time() - start)

print(len(list_data))
















# id - id пользователя
#
# first_name - имя
#
# last_name - фамилия
#
# deactivated - Поле возвращается, если страница пользователя удалена или заблокирована, содержит значение deleted или banned. В этом случае опциональные поля не возвращаются.
#
# is_closed - Скрыт ли профиль пользователя настройками приватности.
#
# bdate - Дата рождения. Возвращается в формате D.M.YYYY или D.M (если год рождения скрыт). Если дата рождения скрыта целиком, поле отсутствует в ответе.
#
# city - место жительства
#
# home_town - Название родного города.





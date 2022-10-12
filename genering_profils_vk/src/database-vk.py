#! /usr/bin/python
# -*- coding: utf-8 -*-
import asyncio
from aiohttp import ClientSession
import nest_asyncio
from time import time
import vk_api
from pprint import pprint
import os
import requests
import json
from genering_profils_vk.src.func import *
import sys
import json
import os
from shutil import rmtree
from time import sleep, time
from genering_profils_vk.src import config
from datetime import datetime
try:
    from urllib import urlopen as urlopen
    from urllib import urlencode as urlencode
except ImportError:
    from urllib.request import urlopen as urlopen
    from urllib.parse import urlencode as urlencode

list_data = []
list_token = []
with open(os.path.join("..", "tokens", "list_tokens_new.txt"), 'r') as f:
    for line in f:
        list_token.append(str(line).rstrip('\n'))

def download_inf_users(list_token):
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
            param3200 = 260000
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
    threshold = 3
    for i in range(threshold):
        param_count = 40
        for query in range(i * param_count + 1, (i + 1) * param_count + 1):
            print(query, time()-st)
            st = time()
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(run_zero(query))


download_inf_users(list_token)


string = json.dumps(list_data)
# print(string)
# data = json.loads(string)
with open("database-VK-users.txt", "w", encoding="utf-8") as file:
    file.write(string)

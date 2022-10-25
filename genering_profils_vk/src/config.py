import os
from pprint import pprint

from django.db.models import Q

from Site.models import CorruptInfo, TokensForVkUpdate, TokenAdmin

token = str(TokenAdmin.objects.order_by("tokenVK").last())

dict_word = {}
word_list = list(CorruptInfo.objects.all().values())
for word in word_list:
    if isinstance(word, dict):
        dict_word[word.get("value", "")] = word.get("info", "")

list_token = [dict_token.get("tokenVK", "") for dict_token in list(TokensForVkUpdate.objects.all().values())]

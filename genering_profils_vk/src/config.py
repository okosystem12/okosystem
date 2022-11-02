import os
from pprint import pprint

from django.db.models import Q

from Site.models import CorruptInfo, TokensForVkUpdate, TokenAdmin

token = str(TokenAdmin.objects.order_by("tokenVK").last())
list_token = [dict_token.get("tokenVK", "") for dict_token in list(TokensForVkUpdate.objects.all().values())]

from django.db.models import Q


def search(oList, word):
    return oList.filter(
        Q(value__icontains=word)
        | Q(info__icontains=word)
    )

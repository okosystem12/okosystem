from django.db.models import Q


def search(oList, word):
    return oList.filter(
        Q(number__icontains=word)
    )

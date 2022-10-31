from django.db.models import Q


def fJoin(word):
    return (
            Q(social__controlUser__lastName__icontains=word)
            | Q(social__controlUser__firstName__icontains=word)
            | Q(social__controlUser__patronymic__icontains=word)
            | Q(social__prefix__icontains=word)
            | Q(social__value__icontains=word)
    )

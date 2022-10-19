from django.db.models import Q


def search(oList, word):
    return oList.filter(
        Q(lastName__icontains=word)
        | Q(firstName__icontains=word)
        | Q(patronymic__icontains=word)
        | Q(updatedAt__icontains=word)
        | Q(birthDay__icontains=word)
        | Q(birthMonth__icontains=word)
        | Q(birthYear__icontains=word)
        | Q(phone__value__icontains=word)
        | Q(mail__value__icontains=word)
        | Q(birthPlace__country__title__icontains=word)
        | Q(birthPlace__region__title__icontains=word)
        | Q(birthPlace__city__title__icontains=word)
        | Q(livePlace__country__title__icontains=word)
        | Q(livePlace__region__title__icontains=word)
        | Q(livePlace__city__title__icontains=word)
        | Q(schools__icontains=word)
        | Q(universities__icontains=word)
        | Q(work__icontains=word)
        | Q(vch__number__icontains=word)
    )

from operator import itemgetter


def sortList(list_to_be_sorted, key, direction=False):
    return sorted(list_to_be_sorted, key=itemgetter(key), reverse=direction)

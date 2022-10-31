import functools


def sortListCustom(list_to_be_sorted, compare_funk, direction):
    for i in range(len(list_to_be_sorted)):
        for j in range(i + 1, len(list_to_be_sorted)):
            if (compare_funk(list_to_be_sorted[i], list_to_be_sorted[j]) * (1 if direction else -1)) == 1:
                list_to_be_sorted[i], list_to_be_sorted[j] = list_to_be_sorted[j], list_to_be_sorted[i]

    return list_to_be_sorted

from random import randint


def quick_sort(lst, left_edge, right_edge):
    if left_edge < right_edge:
        left, right = partition(lst, left_edge, right_edge)
        quick_sort(lst, left_edge, left - 1)
        quick_sort(lst, right + 1, right_edge)

    return lst


def partition(lst, left_edge, right_edge):
    t = randint(0, len(lst) - 1)
    x = lst[t]

    temp = lst[t]
    lst[t] = lst[left_edge]
    lst[left_edge] = temp

    j = left_edge
    k = j
    for i in range(left_edge + 1, right_edge + 1):
        if lst[i] < x:
            j += 1
            k += 1
            temp = lst[j]
            lst[j] = lst[i]
            lst[i] = temp
        elif lst[i] == x:
            k += 1
            temp = lst[k]
            lst[k] = lst[i]
            lst[i] = temp

    temp = lst[j]
    lst[j] = lst[left_edge]
    lst[left_edge] = temp
    return j, k

def counting_sort(lst, n):
    temp = [0] * n
    res = [0] * len(lst)

    for element in lst:
        temp[element] += 1

    for i in range(1, n):
        temp[i] += temp[i - 1]

    for j in range(len(lst) - 1, -1, -1):
        res[temp[lst[j]] - 1] = lst[j]
        temp[lst[j]] -= 1

    return res


def main():
    n = int(input())
    a = [int(element) for element in input().split()]

    print(*counting_sort(a, 11))


if __name__ == '__main__':
    main()

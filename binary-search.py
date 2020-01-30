def binary_search(lst, key):
    ls, rs = 0, len(lst) - 1

    while ls <= rs:
        mid = (ls + rs) // 2
        if lst[mid] == key:
            return mid + 1
        elif lst[mid] > key:
            rs = mid - 1
        else:
            ls = mid + 1
    return -1


def main():
    n, *a = map(int, input().split())
    k, *b = map(int, input().split())

    for i in range(k):
        print(binary_search(a, b[i]), end=' ')


if __name__ == '__main__':
    main()

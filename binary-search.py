def binary_search(n, lst, key):
    ls = 0
    rs = n - 1

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
    st = ''

    for i in range(k):
        print(binary_search(n, a, b[i]), end=' ')


if __name__ == '__main__':
    main()

def inversions_number(lst):
    inv_counter = 0

    while len(lst) > 1:

        if len(lst) % 2 == 1:
            lst.append([10**10])

        temp = []

        for k in range(0, len(lst), 2):
            left = lst[k]
            right = lst[k + 1]
            res = []
            i = 0
            j = 0

            while True:
                if i == len(left):
                    res += right[j::]
                    break
                elif j == len(right):
                    res += left[i::]
                    break

                if left[i] > right[j]:
                    inv_counter += len(left) - i
                    res.append(right[j])
                    j += 1
                else:
                    res.append(left[i])
                    i += 1

            temp.append(res)

        lst = temp

    return inv_counter


def main():
    n = int(input())

    lst = [int(element) for element in input().split()]

    print(inversions_number(lst))


if __name__ == '__main__':
    main()

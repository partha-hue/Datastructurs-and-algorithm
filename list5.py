def leader(arr):
    res = []
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                break

        else:
            res.append(arr[i])

    return res


if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    res = leader(arr)
    print(" ".join(map(str, res)))

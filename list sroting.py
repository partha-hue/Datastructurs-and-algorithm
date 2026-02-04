def removeduplicates(arr):
    seen = set()

    idx = 0

    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
            arr[idx] = arr[i]
            idx += 1

    return idx


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    newsize = removeduplicates(arr)

    for i in range(newsize):
        print(arr[i], end=" ")


def remuvedup(arr):
    new = set()
    idx = 0


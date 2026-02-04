# Iterate Python Program to print alternate elements
# of the app
def getAlternates(arr):
    res = []
    for i in range(0, len(arr), 2):
        res.append(arr[i])
    return res


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    res = getAlternates(arr)
    print(" ".join(map(str, res)))


def dosum(arr):
    result = []
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        result.append(current_sum)

    return result


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    a = dosum(arr)
    print(a)


def sum(arr):
    a = []
    b = 0

    for i in range(len(arr)):
        b += arr[i]
        a.append(b)

    return a


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    a = sum(arr)
    print(a)


# The cumulative sum of an array at index i is defined as the sum of all elements of the array from index 0 to index i.
def cumsum(arr):
    result = []
    currentsum = 0

    for num in arr:
        currentsum += num
        result.append(currentsum)

    return result


if __name__ == "__main__":
    arr = [1, -2, 3, 4, -6]
    result = cumsum(arr)
    print(result)


# For an array of integers nums, an identical twin is defined as pair (i, j) where nums[i] is equal to nums[j] and i < j.

def gettwin(num):
    result = 0
    num = len(arr)

    for i in range(num):
        for j in range(i + 1, num):
            if arr[i] == arr[j]:
                result += 1

    return result


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 1, 2, 3]
    print(gettwin(arr))


# Given an array of integers, find the elements which have an even number of digits

def findeven(arr):
    result = []
    n = len(arr)

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            result.append(arr[i])
    return result


if __name__ == "__main__":
    arr = [10, 15, 40, 25, 30]
    print(findeven(arr))

#Given an array, sort it using insertion sort.
#Given an array arr[], the task is to generate all the possible subarrays of the given array.
def subarry(arr):
    result = []
    n = len(arr)

    for i in range(n):
        for j in range(i, n):
            for k in range(i, j+1):
                print(arr[k], end=" ")
            print()

arr = [1, 2, 3, 4]
print("All Non-empty Subarrys:")
subarry(arr)
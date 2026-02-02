#Given an array arr[], check if it is sorted in ascending order or not.
# Equal values are allowed in an array and two consecutive equal values are considered sorted.
def issortedhelper(arr, n):

    if(n == 0 or n == 1):
        return True
    return (arr[n - 1] >= arr[n - 2] and issortedhelper(arr, n - 1))

def issorted(arr):
    n = len(arr)

    return issortedhelper(arr, n)

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]

    if(issorted(arr)):
        print("true")

    else:
        print("false")
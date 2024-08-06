def countRotations(arr, n):
    if (arr[0] > arr[n - 1]):

        for i in range(0, n):

            if (arr[i] > arr[i + 1]):
                return i + 1
    return 0

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
n = len(arr)
print(countRotations(arr, n))

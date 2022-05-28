def bs(arr, low, high, x):
    if high >= low:
        mid = (low+high)//2

        if arr[mid] == x:
            return mid

        if x < arr[mid]:
            return bs(arr, low, mid-1, x)

        if x > arr[mid]:
            return bs(arr, mid+1, high, x)

    else:
        return -1


l = [1, 2, 3, 4, 5, 7, 8, 9]
print(bs(l, 0, len(l)-1, 6))

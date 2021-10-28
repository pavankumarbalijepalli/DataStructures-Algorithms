from typing import Counter


def partition(customList: list, low: int, high: int):
    i = low - 1
    pivot = customList[high]

    for j in range(low, high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]

    customList[i+1], customList[high] = customList[high], customList[i+1]

    return (i+1)


def _quicksort(customList: list, low: int, high: int):
    if low < high:
        p = partition(customList, low, high)
        _quicksort(customList, low, p-1)
        _quicksort(customList, p+1, high)

    return customList


def quicksort(customList: list):
    return _quicksort(customList, 0, len(customList)-1)


# Get Kth largest element in a list
def quickSelect(customList: list, k: int):
    if not customList:
        return customList

    pivot = customList[len(customList)//2]

    # Here, if we interchange left and right values
    # With the same code we get Kth smallest element.
    left = [i for i in customList if i > pivot]
    mid = [i for i in customList if i == pivot]
    right = [i for i in customList if i < pivot]

    L, M = len(left), len(mid)

    if k <= L:
        return quickSelect(left, k)
    if k > L+M:
        return quickSelect(right, k-L-M)
    else:
        return mid[0]


if __name__ == "__main__":
    l = [4, 6, 8, 1, 2, 3, 5, 9, 7, 9, 9, -1, 0, 88, -99]
    print('='*5)
    print(_quicksort(l, 0, len(l)-1))
    print('='*5)

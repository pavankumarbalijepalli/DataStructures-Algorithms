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
    

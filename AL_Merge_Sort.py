
def merge(customList, l, m, r):
    # Finding length of splits
    n1 = m-l+1
    n2 = r-m

    # Preparing Arrays to store splits
    L = [0]*n1
    R = [0]*n2

    # Assigning Values to Arrays
    for i in range(0, n1):
        L[i] = customList[l+i]
    for i in range(0, n2):
        R[i] = customList[m+i+1]

    i, j, k = 0, 0, l

    # Merging them back in sorted order

    # For both Left and Right Cases
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1

    # For only left case
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1

    # For only right case
    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1


def mergeSort(customList, l, r):
    if l < r:
        m = (l+(r-1))//2
        mergeSort(customList, l, m)
        mergeSort(customList, m+1, r)
        merge(customList, l, m, r)

    return customList


if __name__ == "__main__":
    customList = [6, 8, 4, 5, 2, 7, 9, 3, 1]
    print(mergeSort(customList, 0, 8))

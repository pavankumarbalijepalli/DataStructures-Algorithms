def partition(customlist, low, high):

    # Index of smaller element
    i = low - 1

    # Setting Pivot to right most element of the list
    pivot = customlist[high]

    # From left most to right most but one element
    for j in range(low, high):

        # If the value is less than pivot,
        if customlist[j] <= pivot:

            # Increasing smaller element index by 1
            i += 1

            # Put j value into smaller value position
            customlist[i], customlist[j] = customlist[j], customlist[i]

    # Put pivot value into smaller value position
    customlist[i+1], customlist[high] = customlist[high], customlist[i+1]

    # Returning the partition index
    return (i+1)


def _quicksort(customlist, low, high):
    if low < high:
        pi = partition(customlist, low, high)
        _quicksort(customlist, low, pi-1)
        _quicksort(customlist, pi+1, high)

    return customlist


def quicksort(customList):
    return _quicksort(customList, 0, len(customList)-1)


if __name__ == "__main__":

    customList = [6, 8, 4, 5, 2, 7, 9, 3, 1]
    print(quicksort(customList))

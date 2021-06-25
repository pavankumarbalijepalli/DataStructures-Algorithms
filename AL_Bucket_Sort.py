import math
from AL_Insertion_Sort import insertionSort


def bucketSort(nums):
    buckets = round(math.sqrt(len(nums)))
    maxValue = max(nums)
    arr = []

    # Making Buckets
    for i in range(buckets):
        arr.append([])

    # Adding Array values into Buckets
    for j in nums:
        idx = math.ceil(j*buckets/maxValue)
        arr[idx-1].append(j)

    # Sorting Values inside Buckets
    for i in range(buckets):
        arr[i] = insertionSort(arr[i])

    # Merging Values back into Array
    k = 0
    for i in range(buckets):
        for j in range(len(arr[i])):
            nums[k] = arr[i][j]
            k += 1
    return nums


nums = [9, 5, 1, 4, 2, 3, 6, 8, 7]
print(bucketSort(nums))

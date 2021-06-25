def insertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums


if __name__ == "__main__":
    nums = [9, 5, 1, 4, 2, 3, 6, 8, 0, 7]
    print(insertionSort(nums))

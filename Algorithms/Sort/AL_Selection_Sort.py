def selectionSort(nums):
    for i in range(len(nums)):
        midx = i
        for j in range(i+1, len(nums)):
            if nums[midx] > nums[j]:
                midx = j
        nums[i], nums[midx] = nums[midx], nums[i]
    return nums


nums = [9, 5, 1, 4, 2, 3, 6, 8, 0, 7]
print(selectionSort(nums))

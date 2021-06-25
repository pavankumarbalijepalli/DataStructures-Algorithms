import time


def bubblesort(nums):
    for j in range(len(nums)-1):
        for i in range(len(nums)-j-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


nums = [9, 5, 1, 4, 2, 3, 6, 8, 0, 7]
nums = bubblesort(nums)
print(nums)

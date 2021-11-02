# # # # # # # # # # # # # # # # # 
# Longest Palindromic Substring #
# # # # # # # # # # # # # # # # # 
from typing import DefaultDict

def longest_palidromic_substring(s: str):

    if s == "" or len(s) == 1:
        return s
    
    n = len(s)
    maxlen = 0
    maxstr = ""

    for i in range(1, n):

        start = i-1
        end = i

        while start>=0 and end<n and s[start] == s[end]:
            start -= 1
            end += 1
        
        start += 1
        end -= 1
        
        if s[start] == s[end]:
            if maxlen< end-start+1:
                maxlen = end-start+1
                maxstr = s[start:end+1]
        
        start = i-1
        end = i+1

        while start>=0 and end<n and s[start] == s[end]:
            start -= 1
            end += 1
        
        start += 1
        end -= 1
        
        if s[start] == s[end]:
            if maxlen< end-start+1:
                maxlen = end-start+1
                maxstr = s[start:end+1]

    return maxstr

# # # # # # # # # # # # # # # # # 
# Quicksort                     #
# # # # # # # # # # # # # # # # # 
def partition(customList, low, high):
    i = low - 1
    pivot = customList[high]

    for j in range(low, high):
        if customList[j] < pivot:
            i += 1
            customList[j], customList[i] = customList[i], customList[j]
        
    customList[i+1], customList[high] = customList[high], customList[i+1]
    
    return (i+1)

def _quicksort(customList, low, high):
    if low<high:
        pi = partition(customList, low, high)
        _quicksort(customList, low, pi-1)
        _quicksort(customList, pi+1, high)
    return customList

# Quick Select
def quickselect(customList: list, k:int)-> int: 
    if not customList:
        return customList

    pivot = customList[len(customList)//2]

    left = [i for i in customList if i > pivot]
    mid = [i for i in customList if i == pivot]
    right = [i for i in customList if i < pivot]

    L, M = len(left), len(mid)

    if k <= L:
        return quickselect(left, k)
    if k > L+M:
        return quickselect(right, k-L-M)
    else:
        return mid[0]

# Group Anagrams
def groupanagrams(li: list):
    li = [''.join(sorted(i)) for i in li]
    return sorted(li)

# Sum of SubArray = K
def sumSubArray(customList: list, k: int):
    sums = DefaultDict(int)
    sums[0] = 1
    curr = res = 0

    for num in customList:
        curr += num
        res += sums[curr-k]
        sums[curr] += 1
    return res 

# Driver
if __name__ == "__main__":
    print('\n-----quicksort----')
    print(_quicksort([3,4,5,6,-99,0,7,1,1000], 0, 8))
    print('\n-----longestpalindrome in string----')
    print(longest_palidromic_substring("bdads"))
    print('\n-----kth largest element in array----')
    print(quickselect([0,1,2,5,6,73,3,53,2,5,743,1187], 4))
    print('\n-----grouping anagrams----')
    print(groupanagrams(['cat', 'dog', 'tac', 'god', 'act']))
    print('\n-----sum of sub array = k----')
    print(sumSubArray([1,1,1,1], 2))
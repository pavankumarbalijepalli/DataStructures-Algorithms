# Question: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This will store the (target-element) from list
        sum = {}
        
        # Enumerate gives out the element and index of the element
        for idx, i in enumerate(nums):
            
            # If the element is already present in dictionary
            # We return the (idx of the element) with (value of element in dictionary)
            if i in sum:
                return [idx, sum[i]]
            # If not present, we add (target-element) to the dictionary. 
            # This way if this value is present the list, it will be looped and be found.
            # Since we are adding (target-element), we will find the two indexes where the numbers are present.
            else:
                sum[target-i] = idx

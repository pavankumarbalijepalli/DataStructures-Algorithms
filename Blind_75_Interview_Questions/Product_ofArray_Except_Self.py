# Question: https://leetcode.com/problems/product-of-array-except-self/

## Draw it on a book, it will give a clear idea ##

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Get the length of array
        n = len(nums)

        # Create dummy array for output
        out = [1]*n
        
        # Set prod to 1
        prod = 1

        # Traversing from front of the list
        # This will multiply all the prefixes of the value at position i
        for i in range(1, n):
            # Update prod with it's multiplication with previous nums value
            prod *= nums[i-1]
            # Update out[i] with the prod
            out[i] *= prod
        
        prod = 1

        # Traversing from last of the list
        # This will multiply all the suffixes and multiply them to the prefixes of the value at i
        for i in range(n-2, -1, -1):
            # Update prod with it's multiplication with previous nums value
            prod *= nums[i+1]
            # Update out[i] with the prod
            out[i] *= prod
        
        return out
            
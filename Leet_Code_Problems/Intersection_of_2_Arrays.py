# Question: https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # We make the nums1 as the bigger array 
        # so that we make sure to cover all the values in the list.
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        
        # This tracks if the list has seen a element more than once.
        seen = {}
        
        # In the array nums1,
        for i in nums1:
          # If the element is in seen, 
          # we increase the the value of it by 1
          # This represents how many times a value in in nums1
          if i in seen:
                seen[i] += 1
            # If it is unseen, we make its value to 1.
            else:
                seen[i] = 1
        # Output array
        out = []
        
        # In the array nums2,
        for i in nums2:
            # If the value is in seen, i.e, common for nums1 and nums2,
            # And that element's value is greater than equal to 1
            if (i in seen) and seen[i] >=1:
                # We append it to output list and
                out.append(i)
                # Reduce the value of the element by 1.
                seen[i] -= 1
        return out
                    

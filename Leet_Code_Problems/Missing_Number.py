# Question: https://leetcode.com/problems/missing-number/

from typing import List


class Solution:
    def missingNumber(self, nums: List) -> int:

        """
        To get the missing number, all we need to do is get the sum of
        the range of numbers from 0 to N and then subtract it with the sum of
        list provided.

        `[0,1,3] --> N=3;
        sum(0,1,2,3) = 6;
        sum(0,1,3) = 4;
        then 6-4 = 2;
        (The missing number)`

        Sum of range of N values = `n*(n+1)//2` (cuz integer value)
        """

        return (len(nums)*(len(nums)+1)//2) - sum(nums)
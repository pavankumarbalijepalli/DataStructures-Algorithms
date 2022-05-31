# Question: https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        prefix = strs[0]
        strs = strs[1:]
        while strs:
            temp = ""
            while (prefix and strs[0]) and (prefix[0]==strs[0][0]):
                temp += prefix[0]
                prefix = prefix[1:]
                strs[0] = strs[0][1:]
            prefix = temp
            strs = strs[1:]
        return prefix

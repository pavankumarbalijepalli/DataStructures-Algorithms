# Question: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        lefts = ['(', '{', '[']
        whole = ['()', '{}', '[]']
        stack = []
        
        for i in s:
            if i in lefts:
                stack.append(i)
            elif len(stack)!=0:
                temp = stack.pop() + i
                if temp not in whole:
                    return False
            else:
                return False
                
        return len(stack) == 0
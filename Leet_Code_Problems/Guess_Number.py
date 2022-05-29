# Question: https://leetcode.com/problems/guess-number-higher-or-lower/

def guess(number: int, _guess: int):
    if number<_guess:
        return -1
    if number>_guess:
        return 1
    if number==guess:
        return 0

class Solution:
    # Binary Search Solution
    def guessNumber(self, n: int) -> int:
        begin = 1
        end = n
        while begin <= end:
            mid = (begin+end)//2
            g = guess(mid)
            if g == 0:
                return mid

            # if key is lesser than midpoint
            if g == -1:
                end = mid - 1

            # if key is greater than midpoint
            if g == 1:
                begin = mid + 1
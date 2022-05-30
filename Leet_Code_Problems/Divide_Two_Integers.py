# Question: https://leetcode.com/problems/divide-two-integers/

class Solution:
    
    # Might be a bit confusing at first. Kindly add print statements in between code to understand it better.
    # (X << Y) is same as (X * (2**Y)) -- Keep this in mind while reading the code.
    def divide(self, dividend: int, divisor: int) -> int:
        quo = 0
        
        # XOR will return True for same values (can also use '==' for the same)
        neg = ((dividend < 0) ^ (divisor < 0))
        
        # Remove sign from values
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        # From 31 to 0, i.e., integer value varies from 1 to 2^31
        for i in range(31, -1, -1):
            # We shift divisor with (31 to 0) values and check if it less than or equal to dividend. 
            # That way we get what is the maximum multiple of divisor less than dividend.
            if (divisor << i) <= dividend:
                # Then we update the dividend by subtracting the shifted divisor which is less than or equal to dividend
                dividend -= divisor << i
                # Add the 2**i to the quotient. Which will basically add values to quo till the i is 0 and if condition is true.
                quo += 1 << i
        
        # Adding sign to the quotient
        quo = -1*quo if neg else quo
        
        # Putting value in INT range.
        if quo > (2**31-1):
            quo = 2**31-1
        elif quo < (-2**31):
            quo = -2**31
        return quo
                

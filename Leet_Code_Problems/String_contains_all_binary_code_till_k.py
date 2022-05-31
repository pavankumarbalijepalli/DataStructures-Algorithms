# Question: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        # Maximum binary values for a given K bits
        max_bin = 2**k

        # Seen binary values are stored
        seen = set()

        # From 0 to len(s)-k+1 because we are checking 'k' characters at a time
        # This works on a basis of all the binary values with k-bits are unique.
        # That means if all the values of k-bits are present, the length of the 
        # seen set will be equal to 2^k.
        for i in range(n-k+1):

            # Will store binary number of length 'k' from i
            check = s[i: i+k]

            # If this number is not seen previously
            if check not in seen:
                # It is added to seen
                seen.add(check)

                # Since we have found a k-bit unique value, we reduce the amount of
                # unique values that needs to be checked
                max_bin -= 1
            
            # If all the binary values are seen, 
            # then we can return True because we are traversing k-bits at a time
            # and if we found all 2^k unique binary strings in the list,
            # we can say string has all the binary values till k. 
            if max_bin == 0:
                return True
        
        # In alternate case when loop has ended and we have max_bin>0, we return False
        return False
            
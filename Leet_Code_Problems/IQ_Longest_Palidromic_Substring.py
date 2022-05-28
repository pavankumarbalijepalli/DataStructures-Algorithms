def longestPalindrome(self, s: str) -> str:
        # if s isempty or s is single character return s
        if len(s) == 1 or s == "":
            return s
        
        # Setting Variables
        n = len(s)
        maxl = 0
        maxstr = ""
        
        # From first char to last char
        for i in range(1, n):

            # for even length
            start = i-1
            end = i
            
            while start >= 0 and end < n and s[start] == s[end]:
                start -= 1
                end += 1
            
            start += 1
            end -= 1
            
            if s[start] == s[end]:
                if maxl < end - start+1:
                    maxl = end-start+1
                    maxstr = s[start: end+1]
            
            # for odd length
            start = i-1
            end = i+1
            
            while start >= 0 and end < n and s[start] == s[end]:
                start -= 1
                end += 1
            
            start += 1
            end -= 1
            
            if s[start] == s[end]:
                if maxl < end - start+1:
                    maxl = end-start+1
                    maxstr = s[start: end+1]
            
        return maxstr


# Question: https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for note in ransomNote:
            if note in magazine:
                magazine = magazine.replace(note, '', 1)
            else:
                return False
        return True
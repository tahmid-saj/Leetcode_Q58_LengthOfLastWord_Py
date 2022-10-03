class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        max_len = 0
        strs = s.split()
        
        return len(strs[-1])
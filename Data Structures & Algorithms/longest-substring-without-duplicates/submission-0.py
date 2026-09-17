class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        maxLength = 0
        for ch in s:

            if ch not in substr:
                substr += ch
            else:
                while ch in substr:
                    substr = substr[1:]
                substr += ch
            maxLength = max(maxLength, len(substr))
        return maxLength
    

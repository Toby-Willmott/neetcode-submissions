class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": 
            return 0
        l = 0
        r = 1
        longest = 1
        while r < len(s):
            while s[r] in s[l:r]:
                if r - l > longest: 
                    longest = r-l
                l += 1
            r += 1
        if r - l > longest: 
                    longest = r-l
        return longest

        
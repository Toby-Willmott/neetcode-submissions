class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": 
            return 0
        l = 0
        r = 1
        chars = {s[0]}

        longest = 1
        while r < len(s):
            while s[r] in chars:
                if r - l > longest: 
                    longest = r-l
                chars.remove(s[l])
                l += 1    
            
            chars.add(s[r])
            r += 1
            
        if r - l > longest: 
            longest = r-l
        return longest

        
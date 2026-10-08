class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: 
            return s
        longest = -1
        long_str = ""
        for i in range(len(s)): 
            for j in range(i, len(s)): 
                temp = s[i:j+1]
                if temp == temp[::-1]: 
                    if len(temp) >= longest: 
                        longest = len(temp)
                        long_str = temp

        return long_str
                
        
        
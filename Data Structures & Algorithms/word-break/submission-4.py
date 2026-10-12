class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s): True}
        def recursion(i): 
            if i in dp: 
                return dp[i]
            for word in wordDict: 
                if i+len(word) <= len(s) and s[i:i+len(word)] == word: 
                    if recursion(i+len(word)): 
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        
        return recursion(0)
            

        
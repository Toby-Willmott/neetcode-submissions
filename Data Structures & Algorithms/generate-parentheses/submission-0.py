class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(length, num, remaining, cur): 
            if length == n*2: 
                res.append(cur)
                return 
            if remaining >= 1: 
                cur += ")"
                dfs(length+1, num, remaining -1, cur)
                cur = cur[0:len(cur)-1]
            if num < n:
                cur += "("
                dfs(length+1, num + 1, remaining+1, cur)
                cur = cur[0:len(cur)-1]
        dfs(0, 0, 0,"")
        return res

        
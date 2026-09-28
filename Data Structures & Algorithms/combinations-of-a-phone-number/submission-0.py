class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = [] 

        mapping = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}

        def dfs(i, cur): 
            if i == len(digits):
                res.append(cur)
                return
            for letter in mapping[int(digits[i])]: 
                cur += letter 
                dfs(i+1, cur)
                cur = cur[:-1]
        dfs(0, "")
        if res == [""]:
            return []
        return res
            
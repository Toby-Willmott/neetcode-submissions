class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] 

        def dfs(i, cur): 
            if i == len(s): 
                for pal in cur: 
                    if pal != pal[::-1]:
                        return
                res.append(cur.copy())
                return 
            if i!=0: 
                index = len(cur) - 1
                cur[index] += s[i]
                dfs(i+1, cur)
                cur[index] = cur[index][:-1]
                if cur[-1] != cur[-1][::-1]:
                    return
            cur.append(s[i])
            dfs(i+1, cur)
            cur.pop()

        dfs(0, [])
        return res
        
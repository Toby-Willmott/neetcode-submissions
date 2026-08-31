class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = [] 
        candidates.sort()

        def dfs(i, currentList, total): 
            if total == target: 
                output.append(currentList.copy())
                return
            if total > target or i >= len(candidates): 
                return 

            currentList.append(candidates[i])
            dfs(i+1, currentList, total + candidates[i])
            currentList.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, currentList, total)

        dfs(0, [], 0)
        return output


            
        
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = set()

        def dfs(i): 
            if i in visited or i >= len(nums): 
                return False
            if i == len(nums) - 1: 
                return True
            
            for n in range(nums[i], 0, -1): 
                if dfs(i+n): 
                    return True
                visited.add(i+n)
            
            return False
        
        return dfs(0)
        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [[-1] * len(nums) for _ in range(len(nums))]
        
        def dfs(prev, i): 
            if i == len(nums): 
                return 0
            if memo[prev][i] != -1: 
                return memo[prev][i]

            LIS = dfs(prev, i+1)

            if prev == -1 or nums[prev] < nums[i]: 
                LIS = max(LIS, 1 + dfs(i, i+1))
            
            memo[prev][i] = LIS
            return LIS
        
        return dfs(-1, 0)
        
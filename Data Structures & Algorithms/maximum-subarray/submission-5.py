class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        at_dp = [0] * n
        aoa_dp = [0] * n
        
        at_dp[n-1] = aoa_dp[n-1] = nums[n-1]

        for i in range(n-2, -1, -1): 
            at_dp[i] = max(nums[i], nums[i] + at_dp[i+1])
            aoa_dp[i] = max(aoa_dp[i+1], at_dp[i])
        return aoa_dp[0]
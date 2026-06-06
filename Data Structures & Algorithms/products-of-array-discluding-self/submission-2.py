class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for index in range(len(nums)):
            if index != 0: 
                prefix[index] = prefix[index-1] * nums[index-1]

        for index in range(len(nums)-1, -1, -1):
            if index != len(nums)-1: 
                suffix[index] = suffix[index+1] * nums[index+1]

        output = [suffix[index] * prefix[index] for index in range(len(nums))]

        return output
        
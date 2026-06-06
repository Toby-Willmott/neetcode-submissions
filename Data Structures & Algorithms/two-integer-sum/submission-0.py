class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if nums[i] in lookup: 
                if i < lookup[nums[i]]:
                    return [i, lookup[nums[i]]]
                else: 
                    return [lookup[nums[i]], i]
            else: 
                lookup[difference] = i



        
        
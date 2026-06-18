class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1

        while l <= r:
            index = (l + r) // 2
            test = nums[index]
            print(index, test)
            if test < target: 
                l = index + 1
            elif test > target: 
                r = index -1 
            else: 
                return index
            
        return -1
            


            
        
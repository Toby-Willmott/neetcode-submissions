class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1 

        while l < r: 
            mid = l + (r-l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else: 
                l = mid + 1
        
        start = l
        if len(nums) != 1:
            end = (l - 1) % ((len(nums))-1)
        else: 
            end = l
        if target >= nums[start] and target <= nums[-1]:
            l = start
            r = len(nums) - 1
        else: 
            l = 0 
            r = end
        print(l, r)
        while l <= r: 
            mid = l + (r-l)//2
            print(nums[l:r+1], nums[mid])
            if nums[mid] < target: 
                l = mid + 1 
            elif nums[mid] > target: 
                r = mid - 1
            else: 
                return mid
        return -1
            

            
        
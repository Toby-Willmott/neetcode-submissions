class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        distance = r - l
        largest = 0
        while l < r: 
            if heights[l] < heights[r]: 
                if heights[l]*distance > largest:
                    largest = heights[l] * distance
            else: 
                if heights[r]*distance > largest:
                    largest = heights[r] * distance
            
            if heights[l] < heights[r]: 
                l += 1
            else: 
                r -= 1

            distance -= 1
        return largest
                
                



        
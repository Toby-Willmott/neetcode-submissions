class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        leftMost = [-1] * n
        for i in range(n): 
            while stack and heights[stack[-1]] >= heights[i]: 
                stack.pop()
            if stack: 
                leftMost[i] = stack[-1]
            stack.append(i)

        stack = []
        rightMost = [n] * n 
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack: 
                rightMost[i] = stack[-1]
            stack.append(i)

        
        largest = 0 
        for i in range(n): 
            current = heights[i] * (rightMost[i] - leftMost[i] -1)
            
            
            largest = max(current, largest)
        
        return largest

        
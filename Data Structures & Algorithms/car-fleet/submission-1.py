class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sort_pos = []
        stack = []
        for i in range(len(position)): 
            sort_pos.append((position[i], speed[i]))
        
        sort_pos.sort(reverse=True)
        
        for i in range(len(sort_pos)):
            time = (target-sort_pos[i][0]) / sort_pos[i][1]
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() 
            
        return len(stack)



        
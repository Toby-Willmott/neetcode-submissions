class Node: 
    def __init__(self, val, nei):
        self.val = val
        self.neighbor = nei

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:   
        a_to_b = {i: [] for i in range(numCourses)}
        for a,b in prerequisites: 
            a_to_b[a].append(b)
        
        visited = set()

        def dfs(crs):
            if crs in visited: 
                return False
            
            if a_to_b[crs] == []:
                return True

            visited.add(crs)
            for course in a_to_b[crs]:
                if not dfs(course): 
                    return False
            visited.remove(crs)
            a_to_b[crs] = []
            return True
            
        for num in range(numCourses):
            if not dfs(num): 
                return False
            
        return True
        
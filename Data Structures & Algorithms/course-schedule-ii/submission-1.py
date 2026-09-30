class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        a_to_b = {i: [] for i in range(numCourses)}
        visited = [0]*numCourses
        for course, pre in prerequisites: #course to its prerequisites
            a_to_b[pre].append(course)

        order = []

        def dfs(course):
            visited[course] = 1

            for pre in a_to_b[course]:
                if visited[pre] == 0: 
                    if dfs(pre) == False: 
                        return False
                elif visited[pre] == 1: 
                    return False
            
            visited[course] = 3
            order.insert(0, course)
            return True
            


        for i in range(numCourses): 
            if visited[i] == 0: 
                if dfs(i) == False: 
                    return []

        return order
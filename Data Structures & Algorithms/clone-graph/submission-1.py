"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None

        queue = deque() 
        oldToNew = {}
        copy = Node(node.val)
        oldToNew[node] = copy
        queue.append(node)

        def bfs(): 
            while queue: 
                cur = queue.popleft()
                for nei in cur.neighbors: 
                    if nei not in oldToNew:
                        queue.append(nei)
                        copy = Node(nei.val)
                        oldToNew[nei] = copy 
                    oldToNew[cur].neighbors.append(oldToNew[nei])
        
        bfs()
        return oldToNew[node]



            
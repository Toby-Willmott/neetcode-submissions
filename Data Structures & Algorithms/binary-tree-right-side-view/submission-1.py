# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = [] 
        res = [] 

        if root: 
            queue.append(root)
        curr_level = 0

        while queue: 
            len_q = len(queue)
            res.append([])

            for i in range(len_q):
                curr = queue.pop(0)
                res[curr_level].append(curr.val)
                if curr.left: 
                    queue.append(curr.left)

                if curr.right: 
                    queue.append(curr.right)
                
            curr_level += 1
        result = []
        for lis in res: 
            result.append(lis[-1])
        
        return result

        
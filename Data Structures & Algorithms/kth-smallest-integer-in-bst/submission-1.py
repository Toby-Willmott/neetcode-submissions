# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num = 0
        result = []
        res = root.val 

        def walk(node):
            nonlocal num 
            if not node: 
                return
            walk(node.left)
            result.append(node.val)
            walk(node.right)
        
        walk(root)
        return result[k-1]

        


        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num = 0 
        res = root.val

        def walk(node):
            nonlocal num, res
            if not node: 
                return 
            
            walk(node.left)
            if num == k: 
                return 
            num += 1
            if num == k: 
                res = node.val
                return 
            walk(node.right)

        walk(root)
        return res
        
        
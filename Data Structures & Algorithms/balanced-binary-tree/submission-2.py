# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def depth(root):
            if not root: 
                return [True, 0]

            left = depth(root.left)
            right = depth(root.right)

            balanced = (left[1] == right[1] or left[1]+1 == right[1] or left[1] == right[1] + 1) and left[0] and right[0]
            return [balanced, 1 + max(left[1], right[1])]

        return depth(root)[0]
        


            
        
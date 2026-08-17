# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: 
            return 0 
        
        stack = [(root, root.val)]
        num = 0 

        while stack: 
            curr, maxVal = stack.pop()

            if curr.val >= maxVal: 
                num += 1
            
            maxVal = max(curr.val, maxVal)
            if curr.left: 
                stack.append((curr.left, maxVal))
            if curr.right: 
                stack.append((curr.right, maxVal))
            
        return num
            

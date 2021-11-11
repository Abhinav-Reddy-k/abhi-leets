# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def getLH(node):
            c=0
            while node:
                node=node.left
                c+=1
            return c
        
        def getRH(node):
            c=0
            while node:
                node=node.right   
                c+=1
            return c
        
        total = 0
        
        def rec(node):
            if not node:
                return 0
            
            rh = getRH(node)
            lh = getLH(node)
            if rh == lh:
                return (2**rh)-1
            else:
                return 1 + rec(node.left) + rec(node.right)
           
        return rec(root)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
    # Variable to store LCA node.
        self.ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def rec(node):
            if not node:
                return False
            
            left = rec(node.left)
            right = rec(node.right)
            
            
            if (left and right) or (node.val in [p.val,q.val] and (left or right)):
                self.ans = node
            
            if left or right or (node.val in [p.val,q.val]):
                return True
            return False
        
        rec(root)
        return self.ans
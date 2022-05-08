# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = [] 
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            if not node:
                continue
            self.res.append(node.val)
            stack.extend([node.right,node.left])
        return self.res        
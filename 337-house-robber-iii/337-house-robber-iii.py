# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return [0,0]
            l = dfs(node.left)
            r = dfs(node.right)
            
            return [max(l)+max(r),l[0]+r[0]+node.val]
        
        return max(dfs(root))
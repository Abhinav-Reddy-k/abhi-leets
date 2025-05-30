# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal res
            l = dfs(node.left)
            r = dfs(node.right)
            res+=abs(l-r)
            return l+r+node.val
        
        dfs(root)
        return res
        
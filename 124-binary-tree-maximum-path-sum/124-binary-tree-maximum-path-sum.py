# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float(-inf)
        
        def dfs(node):
            nonlocal maxi
            if not node:
                return 0
            
            ml = dfs(node.left)
            mr = dfs(node.right)
            print(node.val,ml,mr)
            
            maxi = max(ml+node.val,mr+node.val,mr+node.val+ml,maxi,node.val)
            
            return max(node.val+ml,node.val+mr,node.val)
        dfs(root)
        return maxi
            
            
            
        
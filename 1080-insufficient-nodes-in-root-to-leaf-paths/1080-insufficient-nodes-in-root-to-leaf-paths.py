# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(root,summ):
            if not root:
                return False
            if not root.left and not root.right:
                if summ+root.val >= limit:
                    return True
                return False
            l = dfs(root.left,summ+root.val)
            r = dfs(root.right,summ+root.val)
            if not l:
                root.left = None
            if not r:
                root.right = None
            
            return l or r
        
        ans = dfs(root,0)
        return root if ans else None

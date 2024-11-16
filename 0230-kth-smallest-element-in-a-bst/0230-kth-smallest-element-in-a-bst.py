# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i=0
        res=None
        def dfs(root):
            
            nonlocal i, res

            if not root:
                return
            
            if dfs(root.left):
                return

            i+=1
            if i == k:
                res = root.val
                
                return True
            
            if dfs(root.right):
                return

        dfs(root)
        
        return res
        
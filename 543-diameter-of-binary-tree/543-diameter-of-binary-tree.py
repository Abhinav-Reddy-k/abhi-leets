# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        out = 0
        
        def dfs(node):
            if not node:
                return 0
            nonlocal out
            leftH = dfs(node.left)
            rightH = dfs(node.right)
            
            out = max(out,leftH+rightH)
            
            return 1+max(leftH,rightH)
        dfs(root)
        return out
        
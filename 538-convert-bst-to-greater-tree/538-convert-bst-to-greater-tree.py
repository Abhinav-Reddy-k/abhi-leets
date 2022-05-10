# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ts = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal ts
            dfs(node.right)
            temp = node.val
            node.val += ts
            ts += temp
            dfs(node.left)
        dfs(root)
        return root
        
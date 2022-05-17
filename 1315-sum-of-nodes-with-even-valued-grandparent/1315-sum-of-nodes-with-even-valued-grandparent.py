# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getGCS(self,root):
        c = []
        gcs = 0
        if root.left:
            c.append(root.left)
        if root.right:
            c.append(root.right)
        for child in c:
            if child.left:
                gcs+=child.left.val
            if child.right:
                gcs+=child.right.val
        return gcs
        
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        out = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal out
            if node.val %2==0:
                out+=self.getGCS(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return out
                
        
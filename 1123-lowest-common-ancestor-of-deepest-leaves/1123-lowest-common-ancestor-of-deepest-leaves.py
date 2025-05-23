# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root: return 0, None
            
            leftMaxDepth, leftNode = dfs(root.left)
            rightMaxDepth, rightNode = dfs(root.right)
            
            if leftMaxDepth == rightMaxDepth:
                return leftMaxDepth + 1, root
            
            elif leftMaxDepth > rightMaxDepth:
                return leftMaxDepth + 1, leftNode
            
            else:
                return rightMaxDepth + 1, rightNode
            
        maxDepth, ancestor = dfs(root)
        return ancestor
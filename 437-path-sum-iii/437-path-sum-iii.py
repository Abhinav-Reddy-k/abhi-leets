# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        if not root:
            return count
        def dfs(node,r):
            if not node:
                return
            nonlocal count
            count += r.count(0)
            if node.left:
                val = node.left.val
                lr = [i-val for i in r] + [targetSum-val]
                dfs(node.left,lr)
            if node.right:
                val = node.right.val
                rr = [i-val for i in r] + [targetSum-val]
                dfs(node.right,rr)
        dfs(root,[targetSum - root.val])
        return count
            
            
                
        
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
            for i in r:
                if i == 0:
                    count +=1
            if node.left:
                val = node.left.val
                lr = []
                for i in r:
                    lr.append(i-val)
                lr.append(targetSum-val)
                dfs(node.left,lr)
            if node.right:
                val = node.right.val
                rr = []
                for i in r:
                    rr.append(i-val)
                rr.append(targetSum-val)
                dfs(node.right,rr)
        dfs(root,[targetSum - root.val])
        return count
            
            
                
        
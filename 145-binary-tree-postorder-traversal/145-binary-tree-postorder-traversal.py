# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        stack = [root]
        res = []
        
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            stack += [node.left,node.right]
        return res[::-1]
        
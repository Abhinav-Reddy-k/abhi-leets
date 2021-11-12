# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        level = [root]
        
        while level:
            res.append([n.val for n in level])
            temp = []
            for n in level:
                temp.extend([n.left,n.right])
            level = [n for n in temp if n]
        return res
        
            
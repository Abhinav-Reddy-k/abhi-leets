# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        prev = None
        while q:
            l = len(q)
            row = []
            for i in range(l):
                c = q.popleft()
                if not c:
                    continue
                row.append(c.val)
                q.append(c.left)
                q.append(c.right)
            if row:
                prev=row
        return sum(prev)
                
            
        
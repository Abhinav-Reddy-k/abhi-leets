# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        l=None
        while q:
            flag = True
            qlen = len(q)
            for i in range(qlen):
                cur = q.popleft()
                if not cur:
                    continue
                if flag:
                    l = cur.val
                    flag = False
                q.append(cur.left)
                q.append(cur.right)
        return l
                
                
        
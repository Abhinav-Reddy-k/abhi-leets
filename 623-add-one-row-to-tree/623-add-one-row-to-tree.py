# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        q = deque([root])
        d=0
        while q:
            qlen = len(q)
            if d==depth-2:
                for node in q:
                    if not node:
                        continue
                    prev_l = node.left
                    prev_r = node.right
                    node.left = TreeNode(val)
                    node.right = TreeNode(val)
                    node.left.left = prev_l
                    node.right.right = prev_r
                break
                    
            for i in range(qlen):
                cur = q.popleft()
                if not cur:
                    continue
                q.append(cur.left)
                q.append(cur.right)
            d+=1
        return root
        
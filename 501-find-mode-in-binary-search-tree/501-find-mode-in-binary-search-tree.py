# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        c = defaultdict(int)
        
        q = deque([root])
        while q:
            n = q.popleft()
            if not n:
                continue
            c[n.val] += 1
            q.append(n.left)
            q.append(n.right)
        
        return [k for k, v in Counter(c).items() if v == max(Counter(c).values())]
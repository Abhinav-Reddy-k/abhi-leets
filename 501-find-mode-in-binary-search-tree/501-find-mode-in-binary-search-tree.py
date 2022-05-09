# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        
        q = deque([root])
        while q:
            n = q.popleft()
            if not n:
                continue
            dic[n.val] += 1
            q.append(n.left)
            q.append(n.right)
        
        max_freq = max(dic.values())
        return [k for k, v in dic.items() if v == max_freq]
        

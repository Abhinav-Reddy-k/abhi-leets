"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque([root])
        while queue:
            qlen = len(queue)
            ln = []
            for i in range(qlen):
                cur = queue.popleft()
                if not cur:
                    continue
                ln.append(cur)
                queue.append(cur.left)
                queue.append(cur.right)
            for j in range(len(ln)-1):
                ln[j].next = ln[j+1]
        return root
                
                
                
                
                    
                
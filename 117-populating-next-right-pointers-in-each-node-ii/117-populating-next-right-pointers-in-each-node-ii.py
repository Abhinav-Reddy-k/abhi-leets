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
    def connect(self, root: 'Node') -> 'Node':
        queue = deque([root])
        while queue:
            qlen = len(queue)
            prev = None
            for i in range(qlen):
                cur = queue.popleft()
                if not cur:
                    continue
                if prev:
                    prev.next = cur
                prev = cur
                queue.append(cur.left)
                queue.append(cur.right)
        return root
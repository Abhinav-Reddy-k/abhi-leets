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
        
        def rec(node):
            if not node:
                return
            if node.left:
                node.left.next =  node.right
            if node.next:
                if node.next.left:
                   if node.right:
                    node.right.next = node.next.left
            rec(node.left)
            rec(node.right)
        rec(root)
        return root
                
                
                
                
                    
                
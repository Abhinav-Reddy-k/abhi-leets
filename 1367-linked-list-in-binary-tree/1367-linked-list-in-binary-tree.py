# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def dfs(node,head):
            if not head:
                return True
            if not node:
                return False
            if not (node.val == head.val):
                return False
            return dfs(node.left,head.next) or dfs(node.right,head.next)
            
        
        def rec(node):
            if not node:
                return False
            if dfs(node,head):
                return True
            if rec(node.left) or rec(node.right):
                return True
            return False
        
        return rec(root)
            
        
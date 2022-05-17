# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sameTree(self,node1,node2):
        if node1 and not node2:
            return False
        if node2 and not node1:
            return False
        if not node1 and not node2:
            return True
        if node1.val != node2.val:
            return False
        return self.sameTree(node1.left,node2.left) and self.sameTree(node1.right,node2.right)
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q=deque([cloned])
        while q:
            cur = q.popleft()
            if not cur:
                continue
            if cur.val == target.val:
                if self.sameTree(cur,target):
                    return cur
            q.append(cur.left)
            q.append(cur.right)
        
        
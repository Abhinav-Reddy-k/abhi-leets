# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushAll(root)
        
    def next(self) -> int:
        temp = self.stack.pop()
        self.pushAll(temp.right)
        return temp.val
        
    def hasNext(self) -> bool:
        return self.stack
        
    def pushAll(self,node):
        while node:
            self.stack.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
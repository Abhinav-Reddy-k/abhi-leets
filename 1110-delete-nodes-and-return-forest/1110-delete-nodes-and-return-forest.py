# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_del = set(to_delete)
        
        
        def helper(root):
            if not root:
                return None
            
            root.left,root.right = helper(root.left),helper(root.right)
            
            if root.val in to_del:
                if root.right:
                    ans.append(root.right)
                if root.left:
                    ans.append(root.left)
                return None
            
            return root
        
        if root.val not in to_del:
            ans.append(root)
        
        helper(root)
        return ans
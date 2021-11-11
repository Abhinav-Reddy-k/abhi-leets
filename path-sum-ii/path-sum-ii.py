# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        
        def dfs(cn,req_s,path):
            if not cn:
                return []
            
            if not cn.left and not cn.right and cn.val == req_s:
                res.append(path+[cn.val])
            if cn.left:
                dfs(cn.left,req_s-cn.val,path+[cn.val])
            if cn.right:
                dfs(cn.right,req_s-cn.val,path+[cn.val])
                
        dfs(root,targetSum,[])
        
        return res


            
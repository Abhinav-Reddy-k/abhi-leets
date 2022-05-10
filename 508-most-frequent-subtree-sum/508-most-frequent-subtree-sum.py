# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        
        def dfs(node):
            if not node:
                return 0
            cur = node.val + dfs(node.left) + dfs(node.right)
            freq[cur] += 1
            return cur
        
        dfs(root)
        return [key for key, value in freq.items() if value == max(freq.values())]
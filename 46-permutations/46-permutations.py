class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        l = len(nums)
        def dfs(i):
            if len(path) == l:
                res.append(path.copy())
            
            for j in range(l):
                if nums[j] not in path:
                    path.append(nums[j])
                    dfs(i+1)
                    path.pop()
                    
        dfs(0)
        return res
        
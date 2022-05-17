class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(i):
            if i >= len(arr):
                return 0
            
            res = 0
            for j in range(i+1,min(i+1+k, len(arr)+1)):
                cur = max(arr[i:j])*(j-i)
                res = max(res,cur+dfs(j))
            return res
        
        return dfs(0)
                
                
                
                
        
        
        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        dp = {}  #(i,s):Bool
        req = sum(nums)//2
        def dfs(i,s):
            if i == len(nums):
                return False
            if s>req:
                return False
            if s==req:
                return True
            if (i,s) in dp:
                return dp[(i,s)]
            
            dp[(i,s)] = dfs(i+1,s+nums[i]) or dfs(i+1,s)
            
            return dp[(i,s)]
        
        return dfs(0,0)
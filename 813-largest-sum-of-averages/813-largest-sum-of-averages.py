class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        dp = {}
        def dfs(i,k):
            if k==1:
                return sum(nums[i:])/(len(nums)-i)
            if (i,k) in dp:
                return dp[(i,k)]
            
            res = float("-inf")
            for j in range(i,len(nums)-k+1):
                cur_avg = sum(nums[i:j+1])/(j+1-i)
                cur_avg += dfs(j+1,k-1)
                res = max(res,cur_avg)
            dp[(i,k)] = res
            return dp[(i,k)]
        return dfs(0,k)
        
        
        
        
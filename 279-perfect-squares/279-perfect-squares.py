class Solution:
    def numSquares(self, n: int) -> int:
        dp = {0:0,1:1,2:2,3:3}
        for i in range(4,n+1):
            dp[i] = float("inf")
            
        for i in range(1,n+1):
            for j in range(i):
                if j*j <= i:
                    dp[i] = min(1+dp[i-(j*j)],dp[i])
                else:
                    break
        print(dp)
        return dp[n]
                    
            
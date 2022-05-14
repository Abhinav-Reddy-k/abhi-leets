class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        dp = {len(s):1}  # (i) : 1/0
        
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i+1)
            if int(s[i:i+2])<=26 and i+1<len(s):
                res+=dfs(i+2)
            dp[i] = res
            return dp[i]
        
        return dfs(0)
            
            
            
        
        
        
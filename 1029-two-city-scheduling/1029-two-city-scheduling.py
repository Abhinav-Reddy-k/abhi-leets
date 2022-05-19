class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)/2
        dp = {} #(i,a,b:min)
        
        def dfs(i,a,b):
            if a == n and b == n:
                return 0
            if a>n or b>n or i>=len(costs):
                return float("inf")
            
            if (i,a,b) in dp:
                return dp[(i,a,b)]
            
            dp[(i,a,b)] = min(costs[i][0]+dfs(i+1,a+1,b),costs[i][1]+dfs(i+1,a,b+1))
            
            return dp[(i,a,b)]
        
        return dfs(0,0,0)
                
            
            
            
from collections import deque

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        
        dp = deque([1,2])
        
        for i in range(n-2):
            dp.append(sum(dp))
            dp.popleft()
            
        return dp[-1]
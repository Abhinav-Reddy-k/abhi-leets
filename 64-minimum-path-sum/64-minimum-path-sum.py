class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        dp = {} #(r,c) : min
        
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return float("inf")
            if r==rows-1 and c==cols-1:
                return grid[r][c]
            if (r,c) in dp:
                return dp[(r,c)]
            
            dp[(r,c)] = grid[r][c] + min(dfs(r,c+1),dfs(r+1,c))
            return dp[(r,c)]
        
        return dfs(0,0)
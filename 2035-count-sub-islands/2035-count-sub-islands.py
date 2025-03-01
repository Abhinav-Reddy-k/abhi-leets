class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows,cols = len(grid1), len(grid1[0])

        visit = set()

        res = 0

        def dfs(i,j):
            if not ( 0<=i<rows and 0<=j<cols ):
                return True
            if (i,j) in visit:
                return True
            if grid2[i][j] == 0:
                return True
            
            visit.add((i,j))
            res = True
            if grid1[i][j] == 0:
                res = False
            res = dfs(i+1,j) and res  
            res = dfs(i,j+1) and res  
            res = dfs(i-1,j) and res  
            res = dfs(i,j-1) and res
            return res

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] and (i,j) not in visit:
                    if dfs(i,j):
                        res += 1
        return res 
        
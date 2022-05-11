class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        visit = set()
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        sizes = {}
        parents = {}
        maxi = float("-inf")
        
        def dfs(i,j):
            stack = deque([])
            visit.add((i,j))
            count = 1
            stack.append((i,j))
            
            while stack:
                row,col = stack.popleft()
                for k,l in dirs:
                    ni,nj = row+k,col+l
                    if (ni in range(rows) and nj in range(cols) and (ni,nj) not in visit and grid[ni][nj] == 1):
                        stack.append((ni,nj))
                        visit.add((ni,nj))
                        parents[(ni,nj)] = (i,j)
                        count+=1
            return count
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visit and grid[i][j] == 1:
                    parents[(i,j)] = (i,j)
                    sizes[(i,j)] = dfs(i,j)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    total = 1
                    p = set()
                    for r,c in dirs:
                        nr,nc = i+r,j+c
                        if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                            if not parents[(nr,nc)] in p:
                                p.add(parents[(nr,nc)])
                                total += sizes[parents[(nr,nc)]]
                    maxi = max(maxi,total)
        return maxi if maxi != float("-inf") else rows*cols
                            
        
        
        
        
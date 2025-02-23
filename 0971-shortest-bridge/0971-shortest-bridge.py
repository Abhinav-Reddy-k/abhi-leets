class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])

        def bfs(i,j):
            res = 0
            visit = set()
            q = collections.deque()
        
            def dfs(i,j):
                if (i,j) in visit or i < 0 or i >= rows or j < 0 or j >= cols:
                    return
                if grid[i][j] == 0:
                    return
                visit.add((i,j))
                q.append((i,j,0))
                for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                    dfs(i+x,j+y)
            
            dfs(i,j)

            while q:
                x,y,d = q.popleft()
                for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if (nx,ny) not in visit and (0<=nx<rows and 0<=ny<cols):
                        if grid[nx][ny] == 1:
                            return d
                        q.append((nx,ny,d+1))
                        visit.add((nx,ny))




        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return bfs(i,j)
        
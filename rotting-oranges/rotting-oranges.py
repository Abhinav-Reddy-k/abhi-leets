from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh,time = 0,0
        
        row,col = len(grid),len(grid[0])
    
        for i in range(row):
            for j in range(col):
                cur =grid[i][j] 
                if  cur== 1:
                    fresh+=1
                if cur == 2:
                    queue.append([i,j])
                    
        d = [[0,1],[1,0],[-1,0],[0,-1]]
        
        while queue and fresh>0:
            for i in range(len(queue)):
                cr,cc = queue.popleft()
                for r,c in d:
                    nr,nc = cr+r,cc+c
                    if nr < 0 or nr >= row or nc < 0 or nc >= col:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] =2
                        fresh-=1
                        queue.append([nr,nc])
            time+=1
        return time if fresh == 0 else -1
        
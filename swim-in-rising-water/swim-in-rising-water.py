class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows,cols=  len(grid),len(grid[0])
        heap = [[grid[0][0],0,0]]
        d = [[0,1],[1,0],[-1,0],[0,-1]]
        visit = set()
        visit.add((0,0))
        while heap:
            mh,r,c = heapq.heappop(heap)
            if (r,c) == (rows-1,cols-1):
                return mh
            for i,j in d:
                nr,nc = r+i,c+j
                if (nr,nc) in visit or nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                heapq.heappush(heap,[max(mh,grid[nr][nc]),nr,nc])
                visit.add((nr,nc))
                
        
        
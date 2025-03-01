class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])

        visit = set()

        h = [(grid[0][0] , (0,0))]
        
        while h:
            curT, curP = heapq.heappop(h)
            if curP in visit:
                continue
            if curP == (rows-1,cols-1):
                return curT
            visit.add(curP)
            x,y = curP
            for nr,nc in [(x+1,y), (x-1,y), (x,y-1), (x,y+1)]:
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visit:
                    newT = max(curT, grid[nr][nc])
                    heapq.heappush(h, (newT , (nr,nc)))
        
                

        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        self.count = sum(grid[i][j] == '1' for i in range(rows) for j in range(cols))
        parent = [i for i in range(rows*cols)]
        
        def find(num):
            if parent[num] != num:
                return find(parent[num])
            return parent[num]
        
        def union(i,j):
            x,y = find(i),find(j)
            if x==y:
                return
            parent[x] = y
            self.count-=1
            
        for i in range(rows):
            for j in range(cols):
                
                if grid[i][j] == "0":
                    continue
                    
                index = i*cols + j
                if j < cols-1 and grid[i][j+1] == '1':
                    union(index, index+1)
                if i < rows-1 and grid[i+1][j] == '1':
                    union(index, index+cols)
                    
        return self.count
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        out = 0
        rows,cols = len(grid), len(grid[0])

        visited = set()

        def bfs(i,j):
            if not ( 0 <= i < rows and 0 <= j < cols ):
                return
            if grid[i][j] == '0' or ((i,j)) in visited:
                return
            visited.add((i,j))

            bfs(i,j+1)
            bfs(i+1, j)
            bfs(i-1,j)
            bfs(i,j-1)
            
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and ((i,j)) not in visited:
                    bfs(i,j)
                    out+=1
        return out
            
class Solution:
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        visit = set()
        count = 0
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(r, c):
            if (r, c) in visit:
                return
            visit.add((r, c))
            for i, j in dirs:
                nr, nc = r+i, c+j
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1":
                    dfs(nr, nc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visit:
                    dfs(i, j)
                    count += 1

        return count
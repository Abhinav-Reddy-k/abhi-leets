class Solution:
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        visit = set()

        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0:
                return 1
            if (r, c) in visit:
                return 0
            visit.add((r, c))
            perimeter = 0
            for i, j in dirs:
                perimeter += dfs(r+i, c+j)
            return perimeter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j)


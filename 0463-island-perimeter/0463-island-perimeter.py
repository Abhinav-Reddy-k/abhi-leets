class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visit = set()
        q = collections.deque()


        # def dfs(i,j):
        #     if not (0<=i<rows and 0<=j<cols):
        #         return 1
        #     if grid[i][j] == 0:
        #         return 1
        #     if (i,j) in visit:
        #         return 0
        #     visit.add((i,j))

        #     return dfs(i+1,j) + dfs(i,j+1) + dfs(i-1,j) + dfs(i,j-1)

        def bfs(i,j):
            res = 0
            while q:
                i,j = q.popleft()
                for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nx,ny = i+x, y+j
                    # If out of bounds, count as a perimeter edge
                    if not (0 <= nx < rows and 0 <= ny < cols):
                        res += 1
                    elif grid[nx][ny] == 0:  # If water, count as a perimeter edge
                        res += 1
                    elif (nx, ny) not in visit:  # If land and not visited, add to queue
                        q.append((nx, ny))
                        visit.add((nx, ny))
            return res



            


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q.append((i,j))
                    visit.add((i,j))
                    return bfs(i,j)

        
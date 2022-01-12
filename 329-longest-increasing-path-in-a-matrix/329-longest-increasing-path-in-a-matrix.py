class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        dp = {}  # (i,j) : lip

        def dfs(i, j, prev):
            if not (0 <= i < rows and 0 <= j < cols and prev < matrix[i][j]):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = 1
            res = max(res, 1 + dfs(i + 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i - 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i, j + 1, matrix[i][j]))
            res = max(res, 1 + dfs(i, j - 1, matrix[i][j]))

            dp[(i, j)] = res
            return res

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, -1)

        return max(dp.values())
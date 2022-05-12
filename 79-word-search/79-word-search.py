class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])
        path = set()
        l = len(word)
        
        def dfs(r,c,i):
            if l == i:
                return True
            if r < 0 or r >= rows or c < 0 or c>= cols or (r,c) in path or board[r][c] != word[i]:
                return False
            
            path.add((r,c))
            res = dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1)
            path.remove((r,c))
            return res
        
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False
                
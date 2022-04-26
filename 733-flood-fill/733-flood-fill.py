class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows,cols = len(image),len(image[0])
        oc = image[sr][sc]
        
        visit = set()
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        
        def dfs(r,c):
            if (r,c) in visit:
                return
            visit.add((r,c))
            image[r][c] = newColor
            for i,j in dirs:
                nr,nc = r+i,c+j
                if not (nr < 0 or nc < 0 or nr == rows or nc == cols):
                    if image[nr][nc] == oc:
                        image[nr][nc] = newColor
                        dfs(nr,nc)
                        
            
            
        dfs(sr,sc)
        return image
        
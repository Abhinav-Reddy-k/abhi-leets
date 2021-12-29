class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights),len(heights[0])
        
        p = set()
        a = set()
        
        pt = [(0,i) for i in range(cols)]+[(i,0) for i in range(rows)]
        at = [(i,cols-1) for i in range(rows)]+[(rows-1,i) for i in range(cols)]
        
        visited = p.union(a)
        
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def dfs(r,c,prev,sets):
            if (r,c) in sets or r < 0 or c < 0 or r >= rows or c >= cols or prev > heights[r][c]:
                    return
            sets.add((r,c))
            for dr,dc in d:
                nr,nc = r+dr,c+dc
                dfs(nr,nc,heights[r][c],sets)
                
        
        for r,c in pt:
            dfs(r,c,heights[r][c],p)
        
        for r,c in at:
            dfs(r,c,heights[r][c],a)
            
        
        return [[i,j] for i,j in p.intersection(a)]
        
        

        
        
        
        
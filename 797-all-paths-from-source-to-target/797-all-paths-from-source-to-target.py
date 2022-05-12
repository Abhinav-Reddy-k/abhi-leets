class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        path = []
        l = len(graph)
        def dfs(i):
            if i == len(graph)-1:
                res.append([*path.copy(),i])
            path.append(i)
            for n in graph[i]:
                dfs(n)
            path.pop()
        dfs(0)
        return res
                
                
                
            
        
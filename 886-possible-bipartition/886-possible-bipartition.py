class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for buddy1, buddy2 in dislikes:
            graph[buddy1].append(buddy2)
            graph[buddy2].append(buddy1)
			
        def dfs(node, group):
            if node in groups:
                if group != groups[node]:
                    return False
            else:
                groups[node] = group
                for nei in graph[node]:
                    if not dfs(nei, group ^ 1):
                        return False
            return True
			
        groups = {}
        for root in graph:
            if root not in groups:
                if not dfs(root, 0):
                    return False
        return True
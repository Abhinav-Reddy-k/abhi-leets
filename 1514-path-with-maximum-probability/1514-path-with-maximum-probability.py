class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = defaultdict(list)
        
        for i in range(len(edges)):
            e=edges[i]
            g[e[0]].append((succProb[i],e[1]))
            g[e[1]].append((succProb[i],e[0]))
            
        visit = set()
        heap = [(-1,start)]
        print(g)
        while heap:
            p,n = heapq.heappop(heap)
            if n in visit:
                continue
            visit.add(n)
            if n == end:
                return -p
            for e in g[n]:
                heapq.heappush(heap,(-abs(p*e[0]),e[1]))
        return 0
        
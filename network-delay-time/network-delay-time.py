class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = collections.defaultdict(list)
        
        for s,d,l in times:
            g[s].append((d,l))
        
        maxT = 0
        
        heap = [(0,k)]
        
        visit = set()
        
        while heap:
            cd,cn = heapq.heappop(heap)
            edges = g[cn]
            
            if cn in visit:
                continue
            
            visit.add(cn)
            maxT = max(maxT,cd)
            
            for d,l in edges:
                if d in visit:
                    continue
                heapq.heappush(heap,(l+cd,d))
        
        return maxT if n == len(visit) else -1
        
        
        
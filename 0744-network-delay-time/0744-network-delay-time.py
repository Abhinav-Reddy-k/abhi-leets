class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        g = {n: [] for n in range(1,n+1)}

        for n1,n2,w in times:
            g[n1].append((n2, w))
        
        h = [(0,k)]

        visit = set()
        
        res = 0
        while h:
            cnw, cn = heapq.heappop(h)
            if cn in visit:
                continue
            visit.add(cn)
            res = max(res, cnw)

            for neiN, neiW in g[cn]:
                if neiN not in visit:
                    heapq.heappush(h,(cnw+neiW, neiN))
                

        return res if len(visit) == n else -1




        
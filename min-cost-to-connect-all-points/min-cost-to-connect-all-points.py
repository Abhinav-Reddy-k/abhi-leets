class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        g = {i:[] for i in range(l)} # i:{[j,c]}
        
        
        for i in range(l):
            x1,y1 = points[i]
            for j in range(i+1,l):
                x2,y2 = points[j]
                md = abs(x2-x1)+abs(y2-y1)
                g[j].append((md,i))
                g[i].append((md,j))
                
        visit = set()
        minH = [[0,0]]
        
        res = 0
        
        while len(visit) < l:
            cost,p = heapq.heappop(minH)
            if p in visit:
                continue
            visit.add(p)
            res+=cost
            for neiC,neiP in g[p]:
                if neiP in visit:
                    continue
                heapq.heappush(minH,[neiC,neiP])
        
        return res
            
        
                
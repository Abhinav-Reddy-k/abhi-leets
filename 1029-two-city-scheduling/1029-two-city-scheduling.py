class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for i in costs:
            diff.append((i[1]-i[0],i[0],i[1]))
        heapq.heapify(diff)
        res = 0
        count_a = 0
        
        while count_a != len(costs)//2:
            cur = heapq.heappop(diff)
            res+=cur[2]
            count_a+=1
        
        for i in diff:
            res+=i[1]
        return res
        
                
            
            
            
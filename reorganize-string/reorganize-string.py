class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        
        heap = [[-cout,char] for char,cout in c.items()]
        
        heapq.heapify(heap)
        
        prev = None
        out = ""
        
        while heap or prev:
            if prev and not heap:
                return ""
            count,char = heapq.heappop(heap)
            count += 1
            out += char
            
            if prev:
                heapq.heappush(heap,prev)
                prev = None
            if count != 0:
                prev = [count,char]
            
        return out
                
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = {k:i for i,k in enumerate(s)}
        
        res= []
        
        ptr = 0
        while ptr<=len(s)-1:
            cur = s[ptr]
            lo = last_occ[cur]
            max_lo = lo
            i=ptr
            while i<max_lo:
                los = last_occ[s[i]]
                max_lo = max(max_lo,los)
                i+=1
            res.append(max_lo+1)
            ptr=max_lo+1
        
        for i in range(len(res)-1,0,-1):
            res[i]-=res[i-1]
        return res
                
            
        
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res = []
        
        if len(s) > 12:
            return res
        
        def bk(i,dots,out):
            if dots == 4 and i == len(s):
                res.append(out[:-1])
            
            if dots == 4:
                return
            
            for j in range(i,min(i+3,len(s))):
                if int(s[i:j+1]) < 256 and (s[i] != "0" or i==j):
                    bk(j+1,dots+1,out+s[i:j+1]+".")
                    
        bk(0,0,"")
            
        return res
                        
        
class Solution:
    def isPal(self,string,l,r):
            while l<r:
                if string[l] == string[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True
        
    def partition(self, s: str) -> List[List[str]]:
        res= []
        path = []
        
        def dfs(i):
            if i>=len(s):
                res.append(path.copy())
            for j in range(i,len(s)):
                if self.isPal(s,i,j):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
        
        dfs(0)
        return res
                    
                
                
            
        
        
        
            
            
        
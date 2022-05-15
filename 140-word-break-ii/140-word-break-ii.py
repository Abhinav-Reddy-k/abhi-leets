class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        path =[]
        
        def dfs(i):
            if i>len(s):
                return
            if i==len(s):
                res.append(path.copy())
            
            for w in wordDict:
                cwl = len(w)
                csw = "".join(s[i:i+cwl])
                if w==csw:
                    path.append(w)
                    dfs(i+cwl)
                    path.pop()
        dfs(0)
        return [" ".join(l) for l in res]
                
        
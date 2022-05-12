class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l = len(nums)
        given = set(nums)
        res = None
        path = []
        
        def dfs(i):
            nonlocal res
            if res:
                return
            if len(path) == l:
                x = "".join(path)
                if x not in given:
                    res = path.copy()
                    return
            if i==0:
                return
            path.append("0")
            dfs(i-1)
            path.pop()
            path.append("1")
            dfs(i-1)
            path.pop()
        dfs(l)
        return "".join(res)
            
        
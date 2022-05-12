class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)
        path = []
        res = []
        l = len(nums)
        def dfs():
            if len(path) == l:
                res.append(path.copy())
            
            for i in c:
                if c[i]:
                    path.append(i)
                    c[i]-=1
                    dfs()
                    path.pop()
                    c[i]+=1
        dfs()
        return res
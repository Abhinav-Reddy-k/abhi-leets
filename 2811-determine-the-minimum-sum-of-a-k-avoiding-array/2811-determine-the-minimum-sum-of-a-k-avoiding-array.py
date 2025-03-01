class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        res = []

        na = set()
        i=1
        while len(res) != n:
            if i not in na:
                na.add(k-i)
                res.append(i)
            i+=1
        
        return sum(res)

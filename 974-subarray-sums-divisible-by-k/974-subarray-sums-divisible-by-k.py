class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        arr = [0]
        for i in nums:
            arr.append(arr[-1]+i)
        arr = [x%k for x in arr]
        c = Counter(arr)
        res = 0
        for i in c:
            if c[i]>=2:
                res += c[i]*(c[i]-1)/2
        return int(res)

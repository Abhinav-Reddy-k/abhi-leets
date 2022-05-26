class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        lenn = len(prices)
        res= lenn
        if lenn==1:
            return res
        l=0
        r=1
        
        while r<lenn:
            if prices[r]-prices[l]==l-r:
                # print(prices[r]-prices[l],r-l)
                # print(l,r)
                r+=1
            else:
                # print(l,r)
                res += (r-l)*(r-l-1)//2
                # print(res)
                l=r
                r+=1
        return res+(r-l)*(r-l-1)//2
        
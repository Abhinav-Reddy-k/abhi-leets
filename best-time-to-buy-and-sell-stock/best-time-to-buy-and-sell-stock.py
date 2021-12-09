class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l,r=0,1
        maxi = 0
        
        while r<len(prices):
            if prices[l] > prices[r]:
                l=r
            else:
                maxi = max(maxi,prices[r]-prices[l])
            r+=1
        
        return maxi
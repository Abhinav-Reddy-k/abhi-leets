class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        
        for i,v in enumerate(prices): 
            while stack and prices[stack[-1]] >= v:
                prices[stack.pop()] -= v
            stack.append(i)

                
        return prices
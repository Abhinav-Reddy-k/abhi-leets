class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        tail = float("-inf")
        
        res = 0
        
        for i,j in pairs:
            if i>tail:
                res+=1
                tail=j
        return res


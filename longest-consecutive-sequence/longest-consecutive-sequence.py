class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums = set(nums)
        maxi = 1
        
        for num in nums:
            if num-1 not in nums:
                cn = num
                m=1
                while cn+1 in nums:
                    m+=1
                    cn+=1
                maxi = max(m,maxi)
        
        return maxi
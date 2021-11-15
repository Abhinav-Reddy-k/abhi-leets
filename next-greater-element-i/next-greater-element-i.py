class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        stack = []
        res = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                d[stack.pop()] = num
            
            stack.append(num)
            
        for num in nums1:
            if num in d:
                res.append(d[num])
            else:
                res.append(-1)
        
        return res
        
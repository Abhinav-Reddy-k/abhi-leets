class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        l = len(nums)
        res = [-1]*l
        for i in range(2*l):
            while stack and nums[stack[-1]] < nums[i%l]:
                res[stack.pop()] = nums[i%l]
            stack.append(i%l) 
        return res
        
        
#         [0]
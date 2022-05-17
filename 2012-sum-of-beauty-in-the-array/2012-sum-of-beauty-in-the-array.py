class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        min_right = [0]*len(nums)
        
        cur_min = float("inf")
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < cur_min:
                cur_min = nums[i]
            min_right[i] = cur_min
        max_left = nums[0]
        res = 0
        for i in range(1,len(nums)-1):
            cur = nums[i]
            if  max_left < cur < min_right[i+1]:
                res+=2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                res+=1
            max_left = max(max_left,cur)
        return res
            
            
            
        
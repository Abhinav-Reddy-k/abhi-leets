class Solution:
    def canJump(self,nums: List[int]) -> bool:
        p1 = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            cur = nums[i]
            if cur >= p1-i:
                p1 = i
        return p1 == 0
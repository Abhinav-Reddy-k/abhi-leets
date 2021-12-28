class Solution:
    def jump(self, nums: List[int]) -> int:
        lastIndex = len(nums)-1
        steps = 0
        l, r = 0, 0
        while r < lastIndex:
            farthestJump = 0
            for i in range(l, r+1):
                farthestJump = max(farthestJump, i+nums[i])
            l = r+1
            r = farthestJump
            steps += 1

        return steps
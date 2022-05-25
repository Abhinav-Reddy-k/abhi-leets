class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s,f=0,0
        
        while True:
            s=nums[s]
            f=nums[nums[f]]
            if s==f:
                break
        print(s,f)
        s=0
        while True:
            s=nums[s]
            f=nums[f]

            if s==f:
                return s
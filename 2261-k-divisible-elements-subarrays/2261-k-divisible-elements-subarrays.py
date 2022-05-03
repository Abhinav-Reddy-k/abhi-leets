class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        v = set()

        for i in range(len(nums)):
            count = 0
            for j in range(i, len(nums)):
                if nums[j] % p == 0:
                    count += 1
                if count > k:
                    break
                v.add(tuple(nums[i:j+1]))

        return len(v)
                    
                
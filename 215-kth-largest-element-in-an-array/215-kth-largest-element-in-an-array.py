class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        res = None
        while k:
            res = heapq.heappop(nums)
            k-=1
        return -res
            
        
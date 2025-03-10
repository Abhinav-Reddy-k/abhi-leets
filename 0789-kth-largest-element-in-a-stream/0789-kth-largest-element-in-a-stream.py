class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.minH, self.k = nums, k
        heapq.heapify(self.minH)
        while len(self.minH) > k:
            heapq.heappop(self.minH)       

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.minH, val)
        if len(self.minH) > self.k:
            heapq.heappop(self.minH)
        return self.minH[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
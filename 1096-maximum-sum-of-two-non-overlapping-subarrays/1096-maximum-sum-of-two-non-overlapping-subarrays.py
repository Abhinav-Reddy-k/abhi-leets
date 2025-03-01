class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def maxSum(firstLen, secondLen):
            n = len(nums)
            prefix = [0] * (n + 1)
            
            # Compute prefix sums
            for i in range(n):
                prefix[i + 1] = prefix[i] + nums[i]
            
            maxFirst = 0  # Maximum sum of firstLen-length subarray seen so far
            result = 0
            
            for i in range(firstLen + secondLen, n + 1):
                # Ensure firstLen subarray is before secondLen subarray
                maxFirst = max(maxFirst, prefix[i - secondLen] - prefix[i - secondLen - firstLen])
                
                # Compute sum of secondLen subarray ending at i
                currentSecond = prefix[i] - prefix[i - secondLen]
                
                # Update the maximum sum of two non-overlapping subarrays
                result = max(result, maxFirst + currentSecond)
            
            return result

    # Check both orders: firstLen before secondLen OR secondLen before firstLen
        return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))
        
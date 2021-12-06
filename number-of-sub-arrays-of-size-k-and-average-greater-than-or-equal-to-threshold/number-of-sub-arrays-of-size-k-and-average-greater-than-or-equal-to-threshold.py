class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *=k
        c=0
        s=sum(arr[0:k])
        for i in range(len(arr)-k+1):
            if s >= threshold:
                c+=1
            if i+k < len(arr):
                s+=(arr[i+k]-arr[i])
                
        return c
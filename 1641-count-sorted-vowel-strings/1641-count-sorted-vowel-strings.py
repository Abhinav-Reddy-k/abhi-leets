class Solution:
    def countVowelStrings(self, n: int) -> int:

        arr = [1]*5
               
        for _ in range(n-1):
            for i in range(1,5):
                arr[i] = arr[i] + arr[i-1]

        return sum(arr)
        
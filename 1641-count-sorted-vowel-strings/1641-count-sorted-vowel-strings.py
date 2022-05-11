class Solution:
    def countVowelStrings(self, n: int) -> int:
        n-=1

        arr = [1]*5


        for j in range(n):
            for i in range(5):
                arr[i] = sum(arr[i:])

        return sum(arr)
        
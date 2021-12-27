class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        l = sum(matchsticks) / 4
        if not l.is_integer():
            return False

        sides = [0]*4

        matchsticks.sort(reverse=True)

        def backtrack(i):
            if i == len(matchsticks):
                return True

            for j in range(len(sides)):
                if sides[j] + matchsticks[i] > l:
                    continue
                sides[j] += matchsticks[i]
                if backtrack(i+1):
                    return True
                sides[j] -= matchsticks[i]
            return False

        return backtrack(0)
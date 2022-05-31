class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        v = set()
        t = 2**k
        
        for i in range(len(s)):
            if i+k <= len(s):
                v.add(s[i:i+k])
        return len(v)==t
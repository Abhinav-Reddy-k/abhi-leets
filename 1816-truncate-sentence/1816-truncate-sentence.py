class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res = []
        i=0
        while k and i<len(s):
            if s[i] == " ":
                k-=1
            res.append(s[i])
            i+=1
        if len(s)!=len(res):
            res.pop()
        return "".join(res)
        
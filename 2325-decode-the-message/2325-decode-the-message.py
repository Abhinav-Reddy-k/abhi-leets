class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        res= {}
        arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        l=0
        for i in range(len(key)):
            if key[i] == ' ':
                continue
            if key[i] in res:
                continue
            if l >= 26:
                break
            res[key[i]] = arr[l]
            l+=1
        x = []
        for i in message:
            x.append(res[i] if i != ' ' else ' ')
        return ''.join(x)
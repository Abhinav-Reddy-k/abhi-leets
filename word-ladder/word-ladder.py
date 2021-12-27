class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:  
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        
        rel = collections.defaultdict(list)
        
        for j in range(len(wordList)):
            for i in range(len(beginWord)):
                pat = wordList[j][:i] + "*" + wordList[j][i+1:]
                rel[pat].append(wordList[j])
        
        res = 1
        
        queue = deque([beginWord])
        mem = [beginWord]
        
        while queue:
            for l in range(len(queue)):
                cw = queue.popleft()
                if cw == endWord:
                    return res
                for i in range(len(cw)):
                    pat = cw[:i] + "*" + cw[i+1:]
                    for mw in rel[pat]:
                        if mw not in mem:
                            mem.append(mw)
                            queue.append(mw)
            res+=1
        return 0
                    
                
                
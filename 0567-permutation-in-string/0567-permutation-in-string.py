class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        s1Count, winCount = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord('a')] += 1
            winCount[ord(s2[i])-ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1Count[i] == winCount[i]:
                matches += 1
        
        
        l=0

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            rightCharIndex = ord(s2[r]) - ord('a')

            winCount[rightCharIndex] += 1
            if s1Count[rightCharIndex] == winCount[rightCharIndex]:
                matches += 1
            elif s1Count[rightCharIndex] + 1 == winCount[rightCharIndex]:
                matches -= 1
            
            
            leftCharIndex = ord(s2[l]) - ord('a')

            winCount[leftCharIndex] -= 1
            if s1Count[leftCharIndex] == winCount[leftCharIndex]:
                matches += 1
            elif s1Count[leftCharIndex] - 1 == winCount[leftCharIndex]:
                matches -= 1

            l+=1
            
            
            
        return matches == 26
            




        
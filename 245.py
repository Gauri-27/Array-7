class Solution(object):
    def shortestWordDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(wordsDict) == 0:
            return -1
        i1 = -1
        i2 = - 1
        min1 = float('inf')
        for i in range(len(wordsDict)):
            if word1 != word2:
                if wordsDict[i] == word1:
                    i1 = i
                if  wordsDict[i] == word2:
                    i2  = i 
            else:
                if wordsDict[i] == word1:
                    i1 = i2
                    i2 = i
                
            if i1 != -1 and i2 != -1:
                min1 = min(min1, abs(i1 -i2))
        return min1

        # TC : O(n)
        # Sc : O(1)

        
        
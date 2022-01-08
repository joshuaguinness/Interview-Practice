class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        shortest_dist = len(wordsDict)
        word1_pos = -1
        word2_pos = -1
        
        for i, v in enumerate(wordsDict):
            if v == word1:
                word1_pos = i
                if word2_pos >= 0:
                    shortest_dist = min(shortest_dist, word1_pos - word2_pos)
            elif v == word2:
                word2_pos = i
                if word1_pos >= 0:
                    shortest_dist = min(shortest_dist, word2_pos - word1_pos)
            
        return shortest_dist
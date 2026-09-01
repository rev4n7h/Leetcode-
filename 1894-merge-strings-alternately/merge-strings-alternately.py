class Solution(object):
    def mergeAlternately(self, word1, word2):
  
        merged = []
        for i in range (min(len(word1),len(word2))):
                merged.append(word1[i])
                merged.append(word2[i])
                
        merged.extend(word1[len(word2):])
        merged.extend(word2[len(word1):])
        return "".join(merged)
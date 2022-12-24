class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=""
        i=0
        while i < len(max(word1,word2,key=len)):
            if i < len(word1):
                merged += word1[i]
            if i < len(word2):
                merged += word2[i]
            i+=1
        return merged
            
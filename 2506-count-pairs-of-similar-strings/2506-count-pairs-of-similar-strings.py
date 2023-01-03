class Solution:
    def similarPairs(self, words: List[str]) -> int:
        set_ = set()
        ans =0
        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j:
                    if set(words[i])==set(words[j]):
                        ans +=1
        return ans//2
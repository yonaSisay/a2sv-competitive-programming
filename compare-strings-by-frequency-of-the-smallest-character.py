class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        countWord = []
        countQuery = []
        ans = []
        for word in words:
            w = sorted(word)
            countWord.append(w.count(w[0]))
        countWord.sort()

        for query in queries:
            q = sorted(query)
            countQuery.append(q.count(q[0]))
        
        for query in countQuery:
            low = 0
            high = len(countWord)

            while low < high:
                mid = low + (high - low) // 2
                if query < countWord[mid]:
                    high = mid 
                else:
                    low = mid + 1
            ans.append(len(words) - low)
        
        return ans
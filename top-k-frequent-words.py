class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mapp = defaultdict(int)
        heap = []
        ans = []
        for word in words:
            mapp[word] -= 1

        for key,val in mapp.items():
            heappush(heap,(val,key))
    
        for _ in range(k):
            temp = heappop(heap)
            ans.append(temp[1])
            
        return ans
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-x for x in piles]
        heapify(heap)

        for _ in range(k):
            x = -heappop(heap)
            heappush(heap, -(x - x//2))
        
        return -sum(heap)
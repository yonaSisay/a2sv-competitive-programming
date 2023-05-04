class Solution:
    def heapify(self, arr, i, n):
        lrg = i
        left = 2*i + 1
        right = 2*i + 2

        if left < n and arr[left] > arr[lrg]:
            lrg = left
        if right < n and arr[right] > arr[lrg]:
            lrg = right
        
        if lrg != i:
            arr[lrg], arr[i] = arr[i], arr[lrg]
            
            self.heapify(arr, lrg, n)

    def max_heap(self , arr , n):
        for i in range(n//2 - 1, -1, - 1):
            self.heapify(arr, i, n)
        
     
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            self.max_heap(stones, len(stones))
            first = heapq.heappop(stones)
            self.max_heap(stones, len(stones))
            second = heapq.heappop(stones)

            z = first - second

            if z:
                heapq.heappush(stones, z)
            
        
        return stones[0] if stones else 0
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        ans = 0
        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                ans = i+1
                continue
            if len(heap) < ladders:
                heappush(heap ,diff)
                ans = i + 1
            elif heap and  heap[0] < diff:
                if bricks >= heap[0]:
                    val  = heappop(heap)
                    bricks -= val
                    ans = i + 1
                    heappush(heap,diff) 
                else:
                    ans = i
                    break
            else:
                if bricks >= diff:
                    ans = i + 1
                    bricks -= diff
                else:
                    break
                
        return ans
import numpy
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:      
        heap = []

        for x in range(len(matrix)):
            for y in range(len(matrix)):
                if len(heap) < k:
                    heappush(heap,-matrix[x][y])
                elif -heap[0] > matrix[x][y]:
                    heappushpop(heap, -matrix[x][y])
        
        return -heap[0]
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        drop = []
        start = []
        
        for i in range(len(trips)):
            drop.append(trips[i][2])
            start.append(trips[i][1])
            
        drop.sort()
        start.sort()
        
        n = drop[-1] - start[0] + 2
        arr = [0] * n
        
        for i in range(len(trips)):
            arr[trips[i][1]] += trips[i][0]
            if trips[i][2] < len(arr):
                arr[trips[i][2]] -= trips[i][0]
        
        prefix = list(accumulate(arr))
        
        if max(prefix) > capacity:
            return False
        
        return True
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans  = [-1] * len(intervals)
        start = []
        
        for i,arr in enumerate(intervals):
            start.append([arr[0],i])
        start.sort()

        for i,interval in enumerate(intervals):
            low = 0
            high = len(intervals)

            while low < high:
                mid = low + (high - low) // 2

                if start[mid][0] >= interval[1]:
                    high = mid
                    ans[i] = start[mid][1]
                else:
                    low = mid + 1
        
        return ans
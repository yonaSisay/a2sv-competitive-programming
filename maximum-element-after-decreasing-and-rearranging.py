class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        m = arr[-1]
        arr[0] = 1
        
        for i in range(len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) > 1:
                if arr[i] + 1 <= m:
                    arr[i + 1] = arr[i] + 1
                else:
                    arr[i + 1] = arr[i]

        return arr[-1]
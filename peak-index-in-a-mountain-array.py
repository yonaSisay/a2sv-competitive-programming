class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        target = max(arr)
        low = 0
        high = len(arr)

        while low < high:
            mid = (low + high) // 2
            if  arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return low
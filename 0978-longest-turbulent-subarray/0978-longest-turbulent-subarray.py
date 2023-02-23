class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxx = 1
        left = 0
        for i in range(len(arr) - 1):
            if arr[i - 1] < arr[i] < arr[i + 1]:
                left = i
            elif arr[i - 1] > arr[i] > arr[i + 1]:  
                left = i
            elif arr[i] == arr[i + 1]:
                left = i + 1
            maxx = max(maxx, i - left + 2)

        return maxx
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = 0      
        for i in range(len(arr)-1,-1,-1):
            if i == len(arr)-1:
                maxi = arr[i]
                arr[i] = -1
                continue
            temp = arr[i]
            arr[i] = maxi
            maxi = max(temp,maxi)
        return arr
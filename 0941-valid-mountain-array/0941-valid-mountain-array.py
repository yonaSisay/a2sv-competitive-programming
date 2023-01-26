class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maxi = 0
        n = len(arr)-1
        if len(arr)<=2:
            return False       
        for  i in range(n):
            if arr[i]>arr[i+1]:
                maxi = i
                break
            elif arr[i]==arr[i+1]:
                return False
        for i in range(maxi,n):
            if arr[i+1] >= arr[i]:
                return False        
        if maxi!=0:
            return True    
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
#         for i in range(len(arr)):
#             for j in range(1,len(arr)-1):
#                 if i!=j :
#                     if  arr[i]==2*arr[j] or arr[j] ==2*arr[i]:
#                         return True
            
#         return False
            nums = {}
            for i in arr:
                if i/2 in nums:
                    return True
                elif i*2 in nums:
                    return True
                nums[i] = 1
            return False
      
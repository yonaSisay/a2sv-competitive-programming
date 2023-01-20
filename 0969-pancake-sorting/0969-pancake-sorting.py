class Solution:
     def pancakeSort(self, arr: List[int]) -> List[int]:
        size = len(arr)
        ans = []
        for i in range(size-1,-1,-1):
            k=0
            if arr[i]==i+1:
                continue
            for j in range(i):
                if arr[j]==i+1:
                    k=j+1
                    break
            right=k-1
            left=0
            while left<right:
                arr[left],arr[right]=arr[right],arr[left]
                left +=1
                right -= 1
            ans.append(k)           
            right = i
            left = 0    
            while left<right:
                arr[left],arr[right]=arr[right],arr[left]
                left +=1
                right -= 1
            ans.append(i+1)
        return ans
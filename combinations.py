class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        nums = [i + 1 for i in range(n)]
    
        def backTrack(arr, idx):
            if len(arr) >= k:
                ans.append(arr)
                return
            
            for i in range(idx,len(nums)):
                arr.append(nums[i])
                backTrack(arr[:], i + 1)
                arr.pop()
            
        backTrack([],0)
        return ans
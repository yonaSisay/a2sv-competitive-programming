class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backTrack(idx, arr):
            if idx >= len(nums):
                return    

            if not arr or arr[-1] <= nums[idx]:
                arr.append(nums[idx])

                if len(arr) >= 2:
                    ans.append(tuple(arr))

                backTrack(idx + 1,arr[:])
                arr.pop()
                
            backTrack(idx + 1, arr[:])
        
        backTrack(0, [])
        return set(ans)
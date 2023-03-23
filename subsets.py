class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def backTrack(idx, arr):
            ans.add(tuple(arr))

            if idx >= len(nums):
                return

            arr.append(nums[idx])
            backTrack(idx + 1, arr[:])
            arr.pop()
            backTrack(idx + 1, arr[:])
            
        backTrack(0, [])

        return ans
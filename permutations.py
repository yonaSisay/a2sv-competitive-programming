class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = 0

        def backTrack(arr):
            nonlocal visited
            if len(arr) >= len(nums):
                ans.append(arr)
                return
            
            for i in range(len(nums)):
                if visited & (1 << i) == 0:
                    arr.append(nums[i])
                    visited |= (1 << i)

                    backTrack(arr[:])
                    visited ^= (1 << i)
                    arr.pop()
       
        backTrack([])

        return ans  
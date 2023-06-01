class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {}
        def solve(n,init):
            if n == len(nums) - 1 and init:
                return nums[n] 
            elif n >= len(nums):
                return 0
            if not init and n == len(nums) - 1:
                return 0
            
            if (n,init) in memo:
                return memo[(n,init)]
            
            notadd = solve(n + 1,init)
            add = solve(n + 2, init)
            memo[(n,init)] = max(notadd,add + nums[n])

            return memo[(n,init)]

        return max(solve(0,0),solve(1,1))
class Solution:
    def mostPoints(self, nums: List[List[int]]) -> int:
        memo = defaultdict(int)

        def dp(idx):
            if idx in memo:
                return memo[idx]
            if idx >= len(nums):
                return 0
            
            use = dp(idx + nums[idx][1] + 1) + nums[idx][0]
            notuse = dp(idx + 1)
            memo[idx] = max(use, notuse)
            
            return memo[idx]
        return dp(0)
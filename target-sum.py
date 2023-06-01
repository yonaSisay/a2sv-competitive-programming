class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo  = {}
        def dp(idx, curtar):
            if (idx,curtar) in memo:
                return memo[(idx,curtar)]

            if idx == len(nums):
                if curtar == target:
                    return 1
                else:
                    return 0
            
            neg = dp(idx + 1, curtar - nums[idx])
            pos = dp(idx + 1, curtar + nums[idx])

            memo[(idx,curtar)] = neg + pos

            return memo[(idx,curtar)]
        
        return dp(0,0)
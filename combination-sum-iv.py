class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        def dp(cursum):
            if cursum in memo:
                return memo[cursum]

            if cursum == 0:
                return 1
            if cursum < 0:
                return 0
            temp = 0

            for num in nums:
                temp += dp(cursum - num)

            memo[cursum] = temp
            
            return temp
        return dp(target)
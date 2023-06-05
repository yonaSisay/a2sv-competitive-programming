class Solution:
    def minimumTotal(self, nums: List[List[int]]) -> int:
        memo = defaultdict(int)

        def dp(row,col):
            if (row,col) in memo:
                return memo[(row,col)]

            if row == len(nums) - 1:
                return nums[row][col]

            same = dp(row + 1, col)
            inc = dp(row + 1, col + 1)
            memo[(row,col)] = min(same,inc) + nums[row][col]

            return memo[(row,col)]
            
        return dp(0,0)
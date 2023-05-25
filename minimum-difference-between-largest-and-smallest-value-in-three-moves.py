class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        n = len(nums) - 1
        change = float('inf')

        for i in range(4):
            change = min(change, nums[n - i] - nums[3 - i])
        return change
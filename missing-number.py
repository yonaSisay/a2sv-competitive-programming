class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
            elif i+1==len(nums):
                return len(nums)
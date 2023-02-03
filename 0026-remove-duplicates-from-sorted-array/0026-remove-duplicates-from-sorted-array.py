class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        first = 0
        second = 1
        
        while second < len(nums):
            if nums[first] == nums[second]:
                nums.pop(second)
                count += 1
                continue
            first += 1
            second += 1
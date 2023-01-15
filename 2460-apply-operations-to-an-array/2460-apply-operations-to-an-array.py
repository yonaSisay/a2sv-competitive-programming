class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        write = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[write]=nums[write],nums[i]
                write +=1
        return nums
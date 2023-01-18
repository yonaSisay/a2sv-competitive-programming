class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0]*n
        for i in range(n):
            for j in range(n):
                if nums[i]>nums[j]:
                    arr[i]+=1
        return arr
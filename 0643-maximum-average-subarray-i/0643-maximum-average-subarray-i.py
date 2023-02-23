class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxx = -float('inf')
        left = 0
        right = k - 1
        summ = sum(nums[left:right + 1]) 
        while right < len(nums):
            maxx = max(summ / k , maxx)
            summ -= nums[left]
            left += 1
            right += 1
            if right < len(nums):
                summ += nums[right]
        return maxx
        
        
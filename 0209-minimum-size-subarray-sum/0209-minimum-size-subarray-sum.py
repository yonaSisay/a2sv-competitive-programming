class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minn = float('inf')
        left = 0
        summ = 0
        
        for i in range(len(nums)):
            summ += nums[i]
            while summ >= target:
                minn = min(minn, i - left + 1)
                summ -= nums[left]
                left += 1
                
        return minn if minn != float('inf') else 0
                
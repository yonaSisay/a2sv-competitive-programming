class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minn = float('inf')
        left = 0
        summ = 0
        right = 0
        while  right < len(nums):
            if summ < target:
                summ += nums[right]
                right += 1
            elif summ >= target:
                minn = min(minn, right - left)
                summ -= nums[left]
                left += 1
            print(summ)
        while summ >= target:
            minn = min(minn, abs(right - left))
            summ -= nums[left]
            left += 1
        return minn if minn != float(inf) else 0
        

                
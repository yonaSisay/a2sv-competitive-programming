class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left = 0
        right = len(nums)-1
        count = 0
        
        while left<right:
            temp = nums[left] + nums[right]
            
            if temp == k:
                # nums.pop(left)
                # nums.pop(right)
                count += 1
                left += 1
                right -= 1
            elif temp < k:
                left += 1
            elif temp > k:
                right -= 1
        return count
                
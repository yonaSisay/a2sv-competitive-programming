class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = high
        while low < high:
            mid = low + (high - low) // 2
            sum = 0

            for num in nums:
                sum += ceil(num / mid)
            
            if sum <= threshold:
                high = mid 
                ans = min(ans,mid)
            else:
                low = mid + 1
        
        return ans
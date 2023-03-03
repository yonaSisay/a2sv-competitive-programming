class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        left = 0
        right = x 

        while left <= right:
            mid = left + (right - left)// 2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid <= x:
                left = mid + 1
                ans = mid
        return ans
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height)-1
        
        while left < right:
            temp =(right - left)*min(height[left],height[right])
            area = max(temp,area)
            if height[left]>height[right]:
                right -= 1
            else:
                left += 1
        return area
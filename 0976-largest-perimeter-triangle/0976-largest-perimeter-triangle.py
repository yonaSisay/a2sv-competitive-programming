class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        largeP = 0
     
        for i in range(0,len(nums)-2):
            if nums[i] < nums[i+1]+nums[i+2]:
                largeP = max(largeP,nums[i]+nums[i+1]+nums[i+2])
        return largeP
                
                
                
        
        
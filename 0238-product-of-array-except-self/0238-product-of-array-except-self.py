class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1]
        back = [1]
        ans = []
        
        for num in nums:
            forward.append(forward[-1] * num)
        for i in range(len(nums) - 1, -1, -1):
            back.append(back[-1] * nums[i])        
           
        back.reverse()
    
        for i in range(len(nums)):
            ans.append(back[i + 1] * forward[i])
        
        return ans
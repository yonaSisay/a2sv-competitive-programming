class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums)-1
        
        while(left<=right):
            if nums[left] == val and nums[right] != val:
                nums[left],nums[right] = nums[right],nums[left]
                left, right = left+1,right-1
            elif nums[left] == val and nums[right] == val:
                right -= 1
            else:
                left += 1
        return left 
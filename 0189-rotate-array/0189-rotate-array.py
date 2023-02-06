class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        n  = size - (k % size)
        arr = nums[n::]
        arr.extend(nums[0:n])
        
        
        for i in range(size):
            nums[i] = arr[i]
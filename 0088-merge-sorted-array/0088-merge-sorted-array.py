class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        right = m-1
        left = n-1
        index = len(nums1) -1
        
        while left >= 0:
            if right == -1:
                nums1[index] = nums2[left]
                left -= 1
                index -= 1
            elif nums1[right] < nums2[left]:
                nums1[index] = nums2[left]
                index -= 1
                left -= 1
            else:
                nums1[index] = nums1[right]
                index -= 1
                right -= 1
        
        
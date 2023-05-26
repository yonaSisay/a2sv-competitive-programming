class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        x = float('inf')
        y = float('inf')

        for num in nums:
            if x >= num:
                x = num
            elif y >= num:
                y = num
            else:
                return True
        return False
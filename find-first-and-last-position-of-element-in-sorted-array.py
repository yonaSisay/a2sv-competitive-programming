class Solution:
    
    def search(self, nums, target, turn):
        l = -1
        r = len(nums)
        best = -1

        while l + 1 < r:
            mid = l + (r - l) // 2
            if turn:
                if nums[mid] < target:
                    l = mid
                else:
                    best = mid
                    r = mid
            else:
                if nums[mid] > target:
                    r = mid
                else:
                    best = mid
                    l = mid
        if nums[best] == target:
            return best
        return -1
    
            

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: 
            return [-1,-1]
        left = self.search(nums, target, True)
        right = self.search(nums, target, False)
        
        return [left,right]
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:    
        nums = []
        for i in range(n):
            nums.append(i+1)
        i = 0
        seen = set()
        count = 0
        while len(seen) != n-1:
            if nums[i%n] not in seen:
                count += 1
            if nums[i%n] not in seen and count == k:
                seen.add(nums[i%n])
                count = 0
            i += 1
            
        for k in range(n):
            if nums[k] not in seen:
                return nums[k]
            
            
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        prefix = list(accumulate(nums))
        mapp = Counter(prefix)
        mapp[0] += 1
        
        for num in prefix:
            if num >= k:
                count += mapp[num - k]
       
        return count
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = list(accumulate(nums))
        mapp = defaultdict(int)
        ans = 0
        mapp[0] = 1
        for num in prefix:
            if num - goal in mapp:
                ans += mapp[num - goal]
            mapp[num] += 1
        
        return ans
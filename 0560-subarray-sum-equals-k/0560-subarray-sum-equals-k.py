class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = [0]
        mapp = defaultdict(int)
        
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        for elm in prefix:
            if elm - k in mapp:
                count += mapp[elm - k] 
            mapp[elm] += 1
        return count
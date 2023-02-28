class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix =  list(accumulate(nums))       
        mapp = defaultdict(int)
        mapp[0] = 1
        
        for i in range(len(prefix)):
            if prefix[i] % k in mapp:
                count += mapp[prefix[i] % k]
            mapp[prefix[i] % k] += 1
        
        return count
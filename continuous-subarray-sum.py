class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = list(accumulate(nums))
        mapp = defaultdict(int)
        mapp[0] = -1

        print(prefix)
        for i,num in enumerate(prefix):
            if num % k in mapp and  i - mapp[num % k] >= 2:
                return True
            if num % k not in mapp:
                mapp[num % k] = i
                
        return False
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mapp = defaultdict(int)
        mapp[0], count, total= 1, 0, 0

        for num in nums:
            total += num
            count += mapp[total % k]
            mapp[total % k] += 1

        return count
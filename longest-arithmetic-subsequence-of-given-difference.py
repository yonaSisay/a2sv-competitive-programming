class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        mapp = defaultdict(int)
        ans = 0
       
        for num in arr:
            temp = num - difference
            mapp[num] = mapp[temp] + 1
            ans = max(ans, mapp[num])

        return ans
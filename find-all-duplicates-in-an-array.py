class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mapp = Counter(nums)
        ans = []
        for num in mapp:
            if mapp[num] > 1:
                ans.append(num)
        return ans
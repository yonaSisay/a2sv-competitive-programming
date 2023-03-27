class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        mapp = Counter(nums)

        for i in range(len(nums)):
            if i + 1 not in mapp:
                ans.append(i + 1)
        return ans
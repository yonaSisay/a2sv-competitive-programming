class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if i%2==0:
                ans.insert(0,i)
            elif i%2!=0:
                ans.append(i)
        return ans
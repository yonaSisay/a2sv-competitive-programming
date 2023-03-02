class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        stack = []
        
        for i in range(2*n):
            while stack and nums[i%n] > nums[stack[-1]]:
                ans[stack[-1]] = nums[i%n]
                stack.pop()
            stack.append(i%n)
        return ans
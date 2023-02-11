class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        ans = [-1] * n
        stack = []
        stack2 = []
        for i in range(n):
            stack.append(i)
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    stack2.append(j)
                while stack and stack2  and stack2[-1] < j and nums2[j] > nums1[stack[-1]]:
                    if nums2[stack2[-1]] == nums1[stack[-1]]:
                        ans[stack[-1]] = nums2[j]
                        stack.pop()
                        stack2.pop()
                    else:
                        break
        return ans
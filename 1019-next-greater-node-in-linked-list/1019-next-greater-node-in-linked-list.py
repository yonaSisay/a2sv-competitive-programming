# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []       
        curr = head
        
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
        ans = [0]*len(nums)
        stack = []
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:    
                ans[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
        return ans
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        num = 101
        while curr:
            if curr.next and curr.val == curr.next.val:
                num = curr.val
            if curr.next and curr.val == num:
                prev.next = curr.next
                curr.next = None
                curr = prev.next  
            elif curr.next == None and curr.val == num:
                prev.next = None
                curr = None            
            else:
                prev = curr
                curr = curr.next
        return dummy.next
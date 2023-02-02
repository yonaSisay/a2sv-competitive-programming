# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        left += 1
        right += 1
        start = None
        end = None
        count = 1
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        
        while curr:
            if count == left - 1:
                start = curr
            elif count == right:
                end = curr.next
                curr.next = None
                break
            count += 1
            curr = curr.next
        
        prev = None
        curr = start.next
        next_ = curr.next
        
        while next_:
            curr.next = prev
            prev = curr
            curr = next_
            next_ = curr.next
        curr.next = prev
        
        
        start.next.next = end
        start.next = curr
        
        return dummy.next
        
        
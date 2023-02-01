# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        if head:
            current = head 
            next_ = current.next
        else:
            return head
        
        while next_:
            current.next = None
            current.next = prev
            prev = current
            current = next_
            next_ = next_.next
        current.next = prev
        return current
                
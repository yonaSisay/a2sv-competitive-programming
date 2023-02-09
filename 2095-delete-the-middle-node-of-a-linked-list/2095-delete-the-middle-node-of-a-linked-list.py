# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        prev = dummy
        curr = head
        next_ = head
        
        while next_ and next_.next:
            prev = prev.next
            curr = curr.next
            next_ = next_.next.next
        prev.next = curr.next
        return dummy.next
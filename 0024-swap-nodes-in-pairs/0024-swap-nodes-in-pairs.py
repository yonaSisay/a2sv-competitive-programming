# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        if not head: return head
      
        prev = dummy
        curr = prev.next
        next_ = curr.next
        
        while curr and next_:
            curr.next = next_.next
            prev.next = next_
            next_.next = curr
#             move the ptr to next nodes
            prev = curr
            curr = curr.next
            if curr:
                next_ = curr.next
        
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        count = 0
        
        while curr:
            curr = curr.next
            count += 1
        
        if count == 1 and n == 1:
            dummy.next = None
        num = count - n
        current = dummy
        i = 1
        while current and i <= num:
            current = current.next
            i += 1
        if current and current.next:
            current.next = current.next.next
        return dummy.next
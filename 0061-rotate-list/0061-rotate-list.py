# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        current = head
        count = 0
        while current:
            current = current.next
            count += 1
        if count == 0:
            return head
        for i in range(k%count):
            curr = dummy.next
            
            while curr and curr.next and curr.next.next:
                curr = curr.next
            
            if curr == None or curr.next == None:
                return head
            
            end = curr.next
            curr.next = None
            end.next = dummy.next
            dummy.next = end
            
        return dummy.next
            
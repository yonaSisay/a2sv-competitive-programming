# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = head
        curr2 = head
        if curr2 and curr2.next == None: return None
        while curr2 and curr2.next:
            curr1 = curr1.next
            curr2 = curr2.next.next
          
            if curr1 and curr2 and curr1 == curr2:
                break
                
        if curr1 != curr2:
            return None
        
        curr1 = head
        
        while curr1 != curr2:
            curr1 = curr1.next
            curr2 = curr2.next
        
        return curr1
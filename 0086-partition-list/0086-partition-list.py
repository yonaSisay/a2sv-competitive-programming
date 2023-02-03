# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        greater = ListNode()
        current = head
        last = None
        
        while current:
            node = ListNode(current.val)
            if current.val >= x:
                curr = greater
                while curr.next != None:
                    curr = curr.next
                curr.next = node
            elif current.val < x:
                curr = less
                while curr.next != None:
                    curr = curr.next
                curr.next = node
                last = node
            current = current.next
        if last:
            last.next = greater.next
        else:
            less.next = greater.next
        return less.next
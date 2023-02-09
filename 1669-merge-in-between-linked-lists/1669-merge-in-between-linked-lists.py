# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0, list1)
        curr = dummy.next
        prev = dummy
        count = 1
        
        while count < a:
            curr = curr.next
            prev = prev.next
            count += 1
        
        dummy2 = ListNode(0,list2)
        cur = dummy2.next
        
        while cur.next:
            cur = cur.next
        
        next_ = curr.next
        curr.next = list2
        
        while count <= b:
            next_ = next_.next
            count += 1
        cur.next = next_
                        
        return dummy.next
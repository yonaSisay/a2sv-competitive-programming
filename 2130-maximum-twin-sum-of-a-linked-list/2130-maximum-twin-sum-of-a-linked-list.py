# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode()
        dummy1 = ListNode(0,head)
        curr = head
        prev = dummy1
        
        while curr and curr.next:
            curr = curr.next.next
            prev = prev.next
            
        dummy.next = prev.next
        prev = None
        
    #   reverse the second linkedlist
    
        curr = dummy.next
        next_ = curr.next
        
        while next_:
            curr.next = prev
            prev = curr
            curr = next_
            next_ = next_.next
        curr.next = prev
        dummy.next = curr
        
    #     calculatet the max of the two sum
    
        curr1 = head
        curr2 = dummy.next
        num = 0
        while curr1 and curr2:
            temp = curr1.val + curr2.val
            num = max(temp,num)
            curr1 = curr1.next 
            curr2 = curr2.next
        
        return num
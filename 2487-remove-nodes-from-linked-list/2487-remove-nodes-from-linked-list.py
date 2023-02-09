# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseNode(self,head):
        dummy = ListNode(0,head)
        prev = None
        curr = dummy.next
        
        if curr.next == None: return head
        
        next_ = curr.next
               
        while next_:
            curr.next = prev
            prev = curr 
            curr = next_
            next_ = next_.next
        curr.next = prev
        dummy.next = curr
        
        return dummy.next
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:    
        dummy = self.reverseNode(head)
        curr = dummy
    
        while curr and curr.next:
            if  curr.val > curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        dummy = self.reverseNode(dummy)
        return dummy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddNode,evenNode = ListNode(),ListNode()
        even = evenNode
        odd =  oddNode
        
        if not head: return
        
        curr =  head
        size = 0
        
        while curr:
            curr = curr.next
            size += 1
        
        curr = head
        nextt = curr.next
        count = 1
        
        while nextt and count <= size:
            if count % 2 == 0:
                curr.next = None
                even.next = curr
                even = even.next
            else:
                curr.next = None
                odd.next = curr
                odd = odd.next
            curr = nextt
            nextt = nextt.next
            count += 1
        
        if size % 2 == 0:
            even.next = curr
        else:
            odd.next = curr
            odd = odd.next
        odd.next = evenNode.next
        
        return oddNode.next
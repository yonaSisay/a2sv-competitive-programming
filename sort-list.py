# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeSort(self, head):
        if head and not head.next:
            return head
        dummy = ListNode(0,head)

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            dummy = dummy.next
        dummy.next = None

        left = self.mergeSort(head)
        right = self.mergeSort(slow)
        
        return self.merge(left , right)
    
    def merge(self, left, right):
        dummy = ListNode()
        curr = dummy

        while left and right:
            if left.val < right.val:
                curr.next = ListNode(left.val)
                left = left.next
            else:
                curr.next = ListNode(right.val)
                right = right.next
            curr = curr.next

        if left:
            curr.next = left
        elif right:
            curr.next = right
        
        return dummy.next



        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        return self.mergeSort(head)
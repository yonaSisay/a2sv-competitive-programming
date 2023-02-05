# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        curr = ans
        
        curr1 = list1
        curr2 = list2
        
        while curr1 or curr2:
            if curr1 and curr2 and curr1.val < curr2.val:
                temp = ListNode(curr1.val)
                curr.next = temp
                curr = curr.next
                curr1 = curr1.next
            elif curr1 and curr2 and curr1.val > curr2.val:
                temp = ListNode(curr2.val)
                curr.next = temp
                curr = curr.next
                curr2 = curr2.next
            elif curr1 and curr2 and curr1.val == curr2.val:
                temp = ListNode(curr1.val)
                temp2 = ListNode(curr2.val)
                
                curr.next = temp
                curr = curr.next
                
                curr.next = temp2
                curr = curr.next
                
                curr2 = curr2.next
                curr1 = curr1.next
            elif curr1 and curr2 == None:
                temp = ListNode(curr1.val)
                curr.next = temp
                curr = curr.next
                curr1 = curr1.next
            elif curr2 and curr1 == None:
                temp = ListNode(curr2.val) 
                curr.next = temp
                curr = curr.next
                curr2 = curr2.next
        return ans.next
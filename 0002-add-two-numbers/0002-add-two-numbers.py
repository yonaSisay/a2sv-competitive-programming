# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        str2 = ""
        ans = ListNode(0)
        
        curr1 = l1
        curr2 = l2
        
        while curr1:
            str1 += str(curr1.val)
            curr1 = curr1.next
        while curr2:
            str2 += str(curr2.val)
            curr2 = curr2.next
        
        str1 = str1[::-1]
        str2 = str2[::-1]
        
        str3 = int(str1) + int(str2)
        str3 = str(str3)[::-1]
        
        curr = ans
        for num in str3:
            node = ListNode(int(num))
            curr.next = node
            curr = curr.next
        return ans.next
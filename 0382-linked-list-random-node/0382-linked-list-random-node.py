# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        
        self.arr_list = []
        self.limit = 0
        
        temp = head
        while temp:
            self.arr_list.append(temp)
            temp = temp.next
            self.limit += 1
        
        
    def getRandom(self) -> int:
        idx = random.randint(0, self.limit - 1)
        return self.arr_list[idx].val
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
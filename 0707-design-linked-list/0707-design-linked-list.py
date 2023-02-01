class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class MyLinkedList:
    
    def __init__(self):
        self.dummy = Node(-1)
        
    def get(self, index: int) -> int:
        count = 0
        current = self.dummy.next
        
        while current and count != index:
            current = current.next
            count += 1       
        if not current:
            return -1
        return current.val
    
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.dummy.next
        self.dummy.next = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        current = self.dummy
        while current.next != None:
            current = current.next
        current.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        current = self.dummy
        count = 0
        while current and count != index:
            current = current.next
            count += 1
        if current:
            node.next = current.next
            current.next = node            
    def deleteAtIndex(self, index: int) -> None:
        current = self.dummy
        count = 0
        while current and count != index:
            current = current.next
            count += 1
        if current and current.next:
            current.next = current.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
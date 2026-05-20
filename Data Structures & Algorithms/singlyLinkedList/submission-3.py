class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if not self.head:
            return -1

        currentNode = self.head

        for i in range(index):
            currentNode = currentNode.next

            if not currentNode:
                return -1

        return currentNode.val

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)

        if not self.head:
            self.head = newNode
            return

        currentNode = self.head

        while currentNode and currentNode.next != None:
            currentNode = currentNode.next

        currentNode.next = newNode

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        currentNode = self.head
        previousNode = None

        for i in range(index):
            if i == index-1:
                previousNode = currentNode

            if not currentNode.next:
                return False

            currentNode = currentNode.next

        previousNode.next = currentNode.next
        return True

    def getValues(self) -> List[int]:
        listValues = []

        currentNode = self.head
        while currentNode:
            listValues.append(currentNode.val)
            currentNode = currentNode.next
        
        return listValues

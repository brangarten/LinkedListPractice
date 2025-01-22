class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
    
    def printValues(self):
        temp = self.head
        
        while temp.next is not None:
            print(temp.value)
            temp = temp.next

        return True

myLL = LinkedList(5)
myLL.printValues

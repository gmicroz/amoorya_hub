class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self) -> None:
        self.head = None


list1 = LinkedList()
print("Head = ", list1.head)

node1 = Node("sunday")
print("data= ", node1.data)
print("next= ", node1.next)
list1.head=node1
print("Head = ", list1.head.data)

list1.head.next = Node("monday")
print(list1)
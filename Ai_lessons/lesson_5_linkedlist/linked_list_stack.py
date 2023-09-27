class Node:
    def __init__(self, data = None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__ (self):
        self.head = None


# بداية البرنامج
node1 = Node(["ahmed","ali","khalid"])
node2 = Node(["salma","hind","reem"])
node3 = Node (["exam"])

Linked_list = LinkedList()

Linked_list.head = node1
Linked_list.head.next = node2
Linked_list.head.next.next = node3


node = Linked_list.head
list_str = ''
while node:
    list_str += str(node.data) + " 👉 "
    node = node.next

print(list_str)

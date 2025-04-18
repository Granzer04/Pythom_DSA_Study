class Node:
    def __init__(self, value): # creates a Node with Value and nothing to point to next
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value): # constructor  SELF is a method inside a class instead a function
        new_node = Node(value) # call the Node class to create a Node
        self.head = new_node
        self.tail = new_node
        self.length = 1
        

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)
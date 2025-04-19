class Node:
    def __init__(self, value): # creates a Node with Value and nothing to point to next
        self.value = value
        self.next = None

class LinkedList:  # CONSTRUCTOR FOR LINKEDLIST 
    def __init__(self, value): # constructor  SELF is a method inside a class instead a function
        new_node = Node(value) # call the Node class to create a Node
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self): # Print Method
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self,value): # Append Method
        new_node = Node(value)
        if self.head is None: # if head of node is None so Node is empty pretty much
            self.head = new_node # Head will = new_node
            self.tail = new_node # 
        else:
            self.tail.next = new_node # setting tail to the next node over which is new node
            self.tail = new_node # Move tail over
        self.length +=1 # Increases size of the LL by 1
        return True        

my_linked_list = LinkedList(1)

my_linked_list.append(2)

my_linked_list.print_list()
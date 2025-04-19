class Node:
    def __init__(self, value):
        self.value = value # The value stored in the Node
        self.next = None # Points to next Node here it points to None so empty

def append(self,value): # pass a value to create new node..
    new_node = Node(value)
    if self.head is None: # if head of node is None so Node is empty pretty much
        self.head = new_node # Head will = new_node
        self.tail = new_node # 
    else:
        self.tail.next = new_node # setting tail to the next node over which is new node
        self.tail = new_node # Move tail over
    self.length +=1 # Increases size of the LL by 1
    return True
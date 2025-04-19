def print_list(self): # Print Method
    temp = self.head
    while temp is not None:
        print(temp.value)
        temp = temp.next
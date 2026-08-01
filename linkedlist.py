class node:
    def __init__(self, value):
        self.data = value
        self.next = None

class linkedlist:
    def __init__(self, value):
        new_node= node(value)
        self.head=new_node
        self.tail= new_node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self, value):
        

my_linked_list=linkedlist(2)
print(my_linked_list.head.value)

    
from .node import Node

class LinkedList:
    def __init__(self):
        self.top = None

    def insert_at_top(self, data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.top is None:
            self.top = new_node
            return

        current = self.top
        while current.next:
            current = current.next

        current.next = new_node

    def delete_from_top(self):
        if self.top is None:
            return
        
        deleted = self.top
        self.top = deleted.next
        return deleted.data
    
    def delete_from_end(self):
        if self.top is None:
            return 

        if self.top.next is None:
            deleted = self.top
            self.top = None
            return deleted.data

        current = self.top
        while current.next.next:
            current = current.next

        deleted = current.next
        current.next = None
        return deleted.data
    
    def display(self):
        print('Stack:', end=' ')
        temp = self.top
        while temp:
            if temp.next:
                print(temp.data, end=' -> ')
            else:
                print(temp.data)

            temp = temp.next
        

    
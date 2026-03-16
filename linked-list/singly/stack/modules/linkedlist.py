from .node import Node

class LinkedList:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        
        popped = self.top
        self.top = popped.next

        self.length -= 1
        return popped.data

    def is_empty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        
        return self.top.data
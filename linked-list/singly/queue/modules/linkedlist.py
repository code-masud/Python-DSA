from .node import Node

class LinkedList:

    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        
        deleted = self.front
        self.front =  deleted.next

        if self.front is None:
            self.rear = None
        
        self.length -= 1
        return deleted.data

    def is_empty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.front.data
    
    def __str__(self):
        values = []
        temp = self.front

        while temp:
            values.append(temp.data)
            temp = temp.next
        return ' -> '.join(values)
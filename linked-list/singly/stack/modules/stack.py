from .linkedlist import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, data):
        self.list.push(data)

    def pop(self):
        return self.list.pop()
    
    def size(self):
        return self.list.size()

    def peek(self):
        return self.list.peek()

    def __str__(self):
        values = []
        temp = self.list.top
        while temp:
            values.append(temp.data)
            temp = temp.next 
        return ' -> '.join(values)
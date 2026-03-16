from .linkedlist import LinkedList


class Queue:

    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, data):
        self.list.enqueue(data)

    def dequeue(self):
        return self.list.dequeue()

    def size(self):
        return self.list.size()

    def peek(self):
        return self.list.peek()

    def __str__(self):
        return f'{self.list}'

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        return ' -> '.join(self.queue)
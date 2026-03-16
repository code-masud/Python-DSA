from modules import Queue

def main():
    q = Queue()

    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')

    print('Queue', q)
    print('Size:',q.size())
    print('Peek:',q.peek())
    
    print('-' * 10)
    print('Popped:',q.dequeue())
    print('-' * 10)

    print('Queue', q)
    print('Size:',q.size())
    print('Peek:',q.peek())


if __name__ ==  '__main__':
    main()
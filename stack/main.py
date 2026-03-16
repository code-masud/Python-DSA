from modules import Stack

class main():
    s = Stack()

    s.push('A')
    s.push('B')
    s.push('C')

    print('Stack:', s)
    print('Size:', s.size())
    print('Peek:', s.peek())
    print('Popped:', s.pop())
    print('Stack:', s)

if __name__ == '__main__':
    main()
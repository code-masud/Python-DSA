from modules import Stack

def main():
    s = Stack()

    s.push('A')
    s.push('B')
    s.push('C')

    print('Stack:', s)
    print('Size', s.size())
    print('Peek:', s.peek())

    print('-'*10)
    print('Popped:', s.pop())
    print('-'*10)
    
    print('Stack:', s)
    print('Size', s.size())
    print('Peek:', s.peek())

if __name__ == '__main__':
    main()


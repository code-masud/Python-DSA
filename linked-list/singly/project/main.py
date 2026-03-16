from modules import LinkedList

def main():
    l = LinkedList()

    l.insert_at_top('A')
    l.insert_at_top('B')

    l.display()

    l.delete_at_position(1)
    # l.insert_at_position('D', 0)
    l.display()

    # l.delete_from_top()
    # l.delete_from_top()

    # l.insert_at_end('E')
    # l.display()

    # # l.insert_at_top('X')
    # # l.insert_at_top('Y')
    # # l.insert_at_top('Z')

    # l.delete_from_end()
    # l.delete_from_end()

    # l.display()
    # l.delete_from_top()
    # l.delete_from_top()
    # l.delete_from_end()
    # l.display()

if __name__ == '__main__':
    main()
import unittest
from modules import Stack


class TestStack(unittest.TestCase):

    def test_stack_initially_empty(self):
        s = Stack()
        self.assertEqual(s.size(), 0)
        self.assertTrue(s.is_empty())

    def test_push(self):
        s = Stack()
        s.push('A')
        s.push('B')
        self.assertEqual(s.peek(), 'B')

    def test_pop(self):
        s = Stack()
        s.push('A')
        s.push('B')
        s.pop()
        self.assertEqual(s.peek(), 'A')

    def test_peek(self):
        s = Stack()
        s.push(5)

        self.assertEqual(s.peek(), 5)

    def test_pop_empty(self):
        s = Stack()

        with self.assertRaises(IndexError):
            s.pop()

    def test_display(self):
        s = Stack()
        s.push("A")
        s.push("B")
        s.push("C")
        self.assertEqual(str(s), 'A -> B -> C')


if __name__ == '__main__':
    unittest.main()

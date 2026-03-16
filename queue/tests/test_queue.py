import unittest
from modules import Queue

class TestQueue(unittest.TestCase):

    def test_Queue_initially_empty(self):
        s = Queue()
        self.assertEqual(s.size(), 0)
        self.assertTrue(s.is_empty())

    def test_enqueue(self):
        s = Queue()
        s.enqueue('A')
        s.enqueue('B')
        self.assertEqual(s.peek(), 'A')

    def test_dequeue(self):
        s = Queue()
        s.enqueue('A')
        s.enqueue('B')
        s.dequeue()
        self.assertEqual(s.peek(), 'B')

    def test_peek(self):
        s = Queue()
        s.enqueue(5)

        self.assertEqual(s.peek(), 5)

    def test_dequeue_empty(self):
        s = Queue()

        with self.assertRaises(IndexError):
            s.dequeue()

    def test_display(self):
        s = Queue()
        s.enqueue("A")
        s.enqueue("B")
        s.enqueue("C")
        self.assertEqual(str(s), 'A -> B -> C')


if __name__ == '__main__':
    unittest.main()
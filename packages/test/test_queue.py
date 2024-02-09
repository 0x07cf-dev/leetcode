import unittest
from packages.ds.Queue import Queue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.assertIsNone(self.queue.peek())
        self.queue.enqueue(5)
        self.assertEqual(self.queue.peek(), 5)
        self.assertEqual(self.queue.length, 1)
        self.queue.enqueue(10)
        self.assertEqual(self.queue.peek(), 5)
        self.assertEqual(self.queue.length, 2)

    def test_deque(self):
        self.assertIsNone(self.queue.deque())
        self.queue.enqueue(5)
        self.queue.enqueue(10)
        self.assertEqual(self.queue.deque(), 5)
        self.assertEqual(self.queue.peek(), 10)
        self.assertEqual(self.queue.length, 1)
        self.assertEqual(self.queue.deque(), 10)
        self.assertIsNone(self.queue.peek())
        self.assertEqual(self.queue.length, 0)

    def test_peek(self):
        self.assertIsNone(self.queue.peek())
        self.queue.enqueue(5)
        self.assertEqual(self.queue.peek(), 5)
        self.queue.enqueue(10)
        self.assertEqual(self.queue.peek(), 5)
        self.queue.deque()
        self.assertEqual(self.queue.peek(), 10)

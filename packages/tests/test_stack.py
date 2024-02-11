import unittest
from packages.dsa.Stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.assertIsNone(self.stack.peek())
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)
        self.assertEqual(self.stack.length, 1)
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)
        self.assertEqual(self.stack.length, 2)

    def test_pop(self):
        self.assertIsNone(self.stack.pop())
        self.stack.push(5)
        self.stack.push(10)
        self.assertEqual(self.stack.pop(), 10)
        self.assertEqual(self.stack.peek(), 5)
        self.assertEqual(self.stack.length, 1)
        self.assertEqual(self.stack.pop(), 5)
        self.assertIsNone(self.stack.peek())
        self.assertEqual(self.stack.length, 0)

    def test_peek(self):
        self.assertIsNone(self.stack.peek())
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 5)

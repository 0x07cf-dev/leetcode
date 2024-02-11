import unittest
from packages.dsa.LinkedList import LinkedList, DoublyLinkedList

'''
class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_length(self):
        self.assertEqual(self.linked_list.length, 0)
        self.linked_list.append(5)
        self.assertEqual(self.linked_list.length, 1)
        self.linked_list.append(10)
        self.assertEqual(self.linked_list.length, 2)

    def test_insert(self):
        self.linked_list.insertAt(0, 5)
        self.assertEqual(self.linked_list.get(0), 5)
        self.linked_list.insertAt(1, 10)
        self.assertEqual(self.linked_list.get(1), 10)
        self.assertEqual(self.linked_list.get(0), 5)
        self.assertEqual(self.linked_list.length, 2)
        with self.assertRaises(IndexError):
            self.linked_list.insertAt(5, 15)

    def test_remove(self):
        self.assertIsNone(self.linked_list.remove(5))
        self.linked_list.append(5)
        self.assertEqual(self.linked_list.remove(5), 5)
        self.assertIsNone(self.linked_list.get(0))

    def test_remove(self):
        with self.assertRaises(IndexError):
            self.linked_list.removeAt(0)
        self.linked_list.append(5)
        self.linked_list.append(10)
        self.assertEqual(self.linked_list.removeAt(1), 10)
        self.assertEqual(self.linked_list.get(0), 5)
        self.assertEqual(self.linked_list.length, 1)
        with self.assertRaises(IndexError):
            self.linked_list.removeAt(5)

    def test_append(self):
        self.linked_list.append(5)
        self.assertEqual(self.linked_list.length, 1)
        self.assertEqual(self.linked_list.get(0), 5)
        self.assertEqual(self.linked_list.length, 1)
        self.linked_list.append(10)
        self.assertEqual(self.linked_list.get(1), 10)
        self.assertEqual(self.linked_list.length, 2)

    def test_prepend(self):
        self.linked_list.prepend(5)
        self.assertEqual(self.linked_list.get(0), 5)
        self.assertEqual(self.linked_list.length, 1)
        self.linked_list.prepend(10)
        self.assertEqual(self.linked_list.get(0), 10)
        self.assertEqual(self.linked_list.get(1), 5)
        self.assertEqual(self.linked_list.length, 2)

    def test_get(self):
        self.assertIsNone(self.linked_list.get(0))
        self.linked_list.append(5)
        self.linked_list.append(10)
        self.assertEqual(self.linked_list.get(0), 5)
        self.assertEqual(self.linked_list.get(1), 10)
        self.assertIsNone(self.linked_list.get(2))


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_prepend(self):
        self.assertIsNone(self.dll.get(0))
        self.dll.prepend(5)
        self.assertEqual(self.dll.get(0), 5)
        self.assertEqual(self.dll.length, 1)
        self.dll.prepend(10)
        self.assertEqual(self.dll.get(0), 10)
        self.assertEqual(self.dll.length, 2)

    def test_insertAt(self):
        self.dll.insertAt(0, 5)
        self.assertEqual(self.dll.get(0), 5)
        self.assertEqual(self.dll.length, 1)
        self.dll.insertAt(1, 10)
        self.assertEqual(self.dll.get(1), 10)
        self.assertEqual(self.dll.length, 2)
        self.dll.insertAt(1, 15)
        self.assertEqual(self.dll.get(1), 15)
        self.assertEqual(self.dll.length, 3)
        with self.assertRaises(IndexError):
            self.dll.insertAt(5, 20)

    def test_append(self):
        self.assertIsNone(self.dll.get(0))
        self.dll.append(5)
        self.assertEqual(self.dll.get(0), 5)
        self.assertEqual(self.dll.length, 1)
        self.dll.append(10)
        self.assertEqual(self.dll.get(1), 10)
        self.assertEqual(self.dll.length, 2)

    def test_remove(self):
        self.assertIsNone(self.dll.remove(5))
        self.dll.append(5)
        self.assertEqual(self.dll.remove(5), 5)
        self.assertIsNone(self.dll.get(0))
        self.assertEqual(self.dll.length, 0)
        self.dll.append(10)
        self.dll.append(15)
        self.assertEqual(self.dll.remove(10), 10)
        self.assertEqual(self.dll.length, 1)
        self.assertEqual(self.dll.remove(15), 15)
        self.assertIsNone(self.dll.get(0))
        self.assertEqual(self.dll.length, 0)

    def test_removeAt(self):
        self.assertIsNone(self.dll.removeAt(0))
        self.dll.append(5)
        self.dll.append(10)
        self.assertEqual(self.dll.removeAt(1), 10)
        self.assertEqual(self.dll.get(0), 5)
        self.assertEqual(self.dll.length, 1)
        self.assertEqual(self.dll.removeAt(0), 5)
        self.assertIsNone(self.dll.get(0))
        self.assertEqual(self.dll.length, 0)

    def test_get(self):
        self.assertIsNone(self.dll.get(0))
        self.dll.append(5)
        self.assertEqual(self.dll.get(0), 5)
        self.dll.append(10)
        self.assertEqual(self.dll.get(1), 10)
        self.assertIsNone(self.dll.get(2))
'''


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert_empty_list(self):
        self.linked_list.insertAt(0, 5)
        self.assertEqual(self.linked_list.get(0), 5)
        self.assertEqual(self.linked_list.length, 1)

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError):
            self.linked_list.insertAt(5, 15)

    def test_insert_middle(self):
        self.linked_list.append(5)
        self.linked_list.append(15)
        self.linked_list.insertAt(1, 10)
        self.assertEqual(self.linked_list.get(1), 10)
        self.assertEqual(self.linked_list.length, 3)

    def test_remove_middle(self):
        self.linked_list.append(5)
        self.linked_list.append(10)
        self.linked_list.append(15)
        self.linked_list.remove(10)
        self.assertEqual(self.linked_list.length, 2)
        self.assertEqual(self.linked_list.get(1), 15)

    def test_remove_last(self):
        self.linked_list.append(5)
        self.linked_list.append(10)
        self.linked_list.remove(10)
        self.assertEqual(self.linked_list.length, 1)
        self.assertIsNone(self.linked_list.get(1))

    def test_remove_first(self):
        self.linked_list.append(5)
        self.linked_list.append(10)
        self.linked_list.remove(5)
        self.assertEqual(self.linked_list.length, 1)
        self.assertEqual(self.linked_list.get(0), 10)


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_insert_empty_list(self):
        self.dll.insertAt(0, 5)
        self.assertEqual(self.dll.get(0), 5)
        self.assertEqual(self.dll.length, 1)

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError):
            self.dll.insertAt(5, 15)

    def test_insert_middle(self):
        self.dll.append(5)
        self.dll.append(15)
        self.dll.insertAt(1, 10)
        self.assertEqual(self.dll.get(1), 10)
        self.assertEqual(self.dll.length, 3)

    def test_remove_middle(self):
        self.dll.append(5)
        self.dll.append(10)
        self.dll.append(15)
        self.dll.remove(10)
        self.assertEqual(self.dll.length, 2)
        self.assertEqual(self.dll.get(1), 15)

    def test_remove_last(self):
        self.dll.append(5)
        self.dll.append(10)
        self.dll.remove(10)
        self.assertEqual(self.dll.length, 1)
        self.assertIsNone(self.dll.get(1))

    def test_remove_first(self):
        self.dll.append(5)
        self.dll.append(10)
        self.dll.remove(5)
        self.assertEqual(self.dll.length, 1)
        self.assertEqual(self.dll.get(0), 10)

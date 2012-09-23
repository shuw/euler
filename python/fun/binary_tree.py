import unittest
from random import random, shuffle


class BinaryTree:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def search(self, key):
        if key < self.key:
            return self.left and self.left.search(key)
        if key > self.key:
            return self.right and self.right.search(key)
        else:
            return self.value

    def insert(self, node):
        if node.key < self.key:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        elif node.key > self.key:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
        else:
            self.value = node.value

    def items(self):
        # depth first travel returns items in order

        if self.left:
            for item in self.left.items():
                yield item

        yield (self.key, self.value)

        if self.right:
            for item in self.right.items():
                yield item


class TestBinaryTree(unittest.TestCase):

    def test_sequential_insert(self):
        root = BinaryTree(0, 0)
        items = [(0, 0)]
        for key in range(1, 100):
            value = random()
            items.append((key, value))
            root.insert(BinaryTree(key, value))

        for key, value in items:
            self.assertEquals(value, root.search(key))

        # items should return sorted list
        for i, item in enumerate(root.items()):
            self.assertEquals(items[i], item)

    def test_random_insert(self):
        root = BinaryTree(0, 0)
        items = [(0, 0)]

        keys = list(range(1, 100))
        shuffle(keys)
        for key in keys:
            value = random()
            items.append((key, value))
            root.insert(BinaryTree(key, value))

        for key, value in items:
            self.assertEquals(value, root.search(key))

        # items should still match and be sorted
        self.assertEquals(sorted(items, key=lambda item: item[0]), list(root.items()))

if __name__ == '__main__':
    unittest.main()

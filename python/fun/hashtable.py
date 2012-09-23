import unittest
from random import random


class Hashtable:

    def __init__(self, size=1000):
        self._size = size
        self._array = [None] * size

    def set(self, key, value):
        index = id(key) % self._size
        items = self._array[index]
        if not items:
            items = self._array[index] = []
        else:
            for i, (k, v) in enumerate(items):
                if k == key:
                    # overriding value
                    items[i] = (key, value)
                    return

        items.append((key, value))

    def get(self, key):
        items = self._array[id(key) % self._size]
        for k, v in items:
            if k == key:
                return v

    def items(self):
        for items in self._array:
            if items:
                for item in items:
                    yield item


class TestHashtable(unittest.TestCase):

    def setUp(self):
        self.table_size = 1000
        self.ht = Hashtable(self.table_size)

    def test_set(self):
        self.assertEquals(set([]), set(self.ht.items()))

        self.ht.set('hello', 'world')
        self.ht.set('cookies', 'cream')

        self.assertEquals(set([
            ('hello', 'world'),
            ('cookies', 'cream')
        ]), set(self.ht.items()))

        # set the same key twice
        self.ht.set('lakes', 'streams')
        self.ht.set('lakes', 'oceans')

        self.assertEquals(set([
            ('hello', 'world'),
            ('cookies', 'cream'),
            ('lakes', 'oceans')
        ]), set(self.ht.items()))

    def test_get(self):
        self.ht.set('hello', 'world1')
        self.assertEquals('world1', self.ht.get('hello'))
        self.ht.set('hello', 'world2')
        self.assertEquals('world2', self.ht.get('hello'))


    def test_collisions(self):
        inserted = []
        for key in xrange(self.table_size * 2): # insert > table_size entries to guarantee collisions
            value = random()
            self.ht.set(key, value)
            inserted.append((key, value))

        for key, value in inserted:
            self.assertEquals(value, self.ht.get(key))

        self.assertEquals(len(list(self.ht.items())), len(inserted))


if __name__ == '__main__':
    unittest.main()

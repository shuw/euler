import unittest
from random import random


class Hashtable:

    def __init__(self, size=1000):
        self.size = size
        self.array = [None] * size

    def __setitem__(self, key, value):
        index = id(key) % self.size
        items = self.array[index]
        if not items:
            items = self.array[index] = []
        else:
            for i, (k, v) in enumerate(items):
                if k == key:
                    # overriding value
                    items[i] = (key, value)
                    return

        items.append((key, value))

    def __getitem__(self, key):
        items = self.array[id(key) % self.size]
        for k, v in items:
            if k == key:
                return v

    def items(self):
        for items in self.array:
            if items:
                for item in items:
                    yield item


class TestHashtable(unittest.TestCase):

    def setUp(self):
        self.table_size = 1000
        self.ht = Hashtable(self.table_size)

    def test_set(self):
        self.assertEquals(set([]), set(self.ht.items()))

        self.ht['hello'] = 'world'
        self.ht['cookies'] = 'cream'

        self.assertEquals(set([
            ('hello', 'world'),
            ('cookies', 'cream')
        ]), set(self.ht.items()))

        # set the same key twice
        self.ht['lakes'] = 'streams'
        self.ht['lakes'] = 'oceans'

        self.assertEquals(set([
            ('hello', 'world'),
            ('cookies', 'cream'),
            ('lakes', 'oceans')
        ]), set(self.ht.items()))

    def test_get(self):
        self.ht['hello'] = 'world1'
        self.assertEquals('world1', self.ht['hello'])
        self.ht['hello'] = 'world2'
        self.assertEquals('world2', self.ht['hello'])

    def test_collisions(self):
        inserted = []
        # insert > table_size entries to guarantee collisions
        for key in xrange(self.table_size * 2):
            value = random()
            self.ht[key] = value
            inserted.append((key, value))

        for key, value in inserted:
            self.assertEquals(value, self.ht[key])

        self.assertEquals(len(list(self.ht.items())), len(inserted))


if __name__ == '__main__':
    unittest.main()

import unittest
from collections import defaultdict


class Hashtable:

    def __init__(self, size=1000):
        self._size = size
        self._table = defaultdict(list)

    def set(self, key, value):
        items = self._table[id(key)]
        for i, (k, v) in enumerate(items):
            if k == key:
                # overriding value
                items[i] = (key, value)
                return

        items.append((key, value))

    def items(self):
        for items in self._table.values():
            for item in items:
                yield item


class TestHashtable(unittest.TestCase):

    def setUp(self):
        self.ht = Hashtable(1000)

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


if __name__ == '__main__':
    unittest.main()

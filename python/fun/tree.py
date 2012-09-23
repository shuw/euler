class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def search(self, key):
        if key < self.key:
            return self.right and self.left.search(key)
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

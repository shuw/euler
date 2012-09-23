class Node:
    def __init__(self, content, next=None):
        self.content = content
        self.next = next

    def __str__(self):
        return str(self.content)


def to_list(node):
    l = []
    while node:
        l.append(node.content)
        node = node.next

    return l


def from_list(l):
    node = None
    for i in reversed(l):
        node = Node(i, node)
    return node


def reverse(node):
    prev = None
    while node:
        tmp = node.next
        node.next = prev
        prev = node
        node = tmp

    return prev


if __name__ == '__main__':
    node = from_list(range(100))

    print(to_list(node))
    print(to_list(reverse(node)))

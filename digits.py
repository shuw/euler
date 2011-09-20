import copy

# Iterates over digits in reverse order
def iterateDigits(n):
    while n > 0:
        yield n % 10
        n /= 10

def toList(n):
    r = []
    while n > 0:
        r.append(n % 10)
        n /= 10
    r.reverse()
    return r

def fromList(nArr):
    n = 0
    for d in nArr:
        n = d + n * 10
    return n

def reverse(n):
    r = 0
    while n > 0:
        r = n % 10 + r * 10
        n /= 10
    return r

def choose(elements, length):
    for i in range(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in choose(elements[i+1:len(elements)], length-1):
                yield (elements[i],) + next

def permutate(elements, length):
    for n in elements:
        if length == 1:
            yield (n,)
        else:
            elements2 = copy.copy(elements)
            elements2.remove(n)
            for next in permutate(elements2, length-1):
                yield (n,) + next

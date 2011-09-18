numbers = []
for key in open('data/p79_keylog.txt'):
    numbers += [int(key)]


# Only care about unique numbers
numbers = set(numbers)

bigrams = []

for n in numbers:
    prevD = None
    for d in str(n):
        d = int(d)
        if (prevD != None): bigrams += [(prevD, d)]
        prevD = d

# Now we have a set of directed edges digit->digit
# we can find the shortest traversal of the entire graph
# or solve it by hand (which is what I did)
edges = set(bigrams)

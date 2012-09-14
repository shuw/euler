import random

def quicksort(l):
    if len(l) <= 1:
        return l

    pivot = l[len(l) / 2]

    left, right = ([], [])
    for index, i in enumerate(l):
        if index == int(len(l) / 2):
            continue
        (left if i <= pivot else right).append(i)

    return quicksort(left) + [pivot] + quicksort(right)


stuff = list(range(100))
random.shuffle(stuff)

print(quicksort(stuff))
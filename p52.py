def sorteddigits(n):
    d = []
    while n > 0:
        d.append(n % 10)
        n = int(n / 10)

    d.sort()
    d.reverse()
    return d

for n in range(1, 1000000):
    nd = sorteddigits(n)

    matched = True
    for k in range(2, 7):
        if sorteddigits(n * k) != nd:
            matched = False
            break;

    if (matched):
        print n
        break

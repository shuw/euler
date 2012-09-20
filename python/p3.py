def findFactors(n):
    if n == 1:
        return;

    i = 2;
    while True:
        if i == n:
            print n;
            return;
        if (n / float(i)) % 1 == 0:
            findFactors(i)
            findFactors(n / i)
            return
        i = i + 1

findFactors(28)

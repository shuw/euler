searchMax = 100000

penNums = set((n*(3*n-1))/2 for n in range (1, searchMax))
hexNums = set((n*(2*n-1)) for n in range (1, searchMax))

triangleNumbers = list((n*(n+1))/2 for n in range (1, searchMax))

for t in triangleNumbers:
    if t in penNums and t in hexNums:
        print t

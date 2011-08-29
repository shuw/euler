import primes

pSet = set(primes.primes(1000000))

# brute-force, but did the trick under 5 minutes
def answer(a):
    maxLength = 0
    for n in [(sum(a[j:i]), (j,i)) for i in range(1,len(a)+1) for j in range(i)]:
        s = n[0]

        length = n[1][1] - n[1][0]
        if n[0] in pSet and length > maxLength:
            maxLength = length
            print str(n[0]) + " " +str(a[n[1][0]:n[1][1]])


answer(primes.primes(10000))

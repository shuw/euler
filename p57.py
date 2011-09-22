# Notice the pattern of numerator and denominator
#   x(n+1) = x(n)*2 + x(n-1) where x(0) == 1
#
# numerator 3 7 17 41 99 239 577 1393
# denominotor 2 5 12 29 70 169 408 985

def seq(n):
    yield n
    pN = 1
    while True:
      temp = n
      n = 2*n + pN
      pN = temp
      yield n

sum = 0
nSeq = seq(3)
dSeq = seq(2)
for i in range(1000):
    n = nSeq.next()
    d = dSeq.next()

    if len(str(n)) > len(str(d)):
        sum += 1

print 'Answer: ' + str(sum)


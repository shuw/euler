def numToArray(n):
    r = []
    while n > 0:
        r.append(n % 10)
        n /= 10
    r.reverse()
    return r

def arrayToNum(nArr):
    n = 0
    for d in nArr:
        n = d + n * 10
    return n

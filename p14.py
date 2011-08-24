

def seq(n):
    if n == 0: return 0
    length = 1
    while n != 1:
        if n % 2 == 0:
            #even
            n = n / 2
        else:
            n = 3*n + 1
        length += 1
    return length

maxLength = 0
for n in reversed(range(1000000)):
    length = seq(n)
    if length > maxLength:
        print str(n) + " length: " + str(length)
        maxLength = length

print maxLength

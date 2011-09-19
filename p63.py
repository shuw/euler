def answer():
    count = 0
    n = 1
    while True:
        for i in range(1, 10):
            if len(str(i**n)) == n: count += 1
            elif i ==9: return count
        n += 1

print 'Answer: ' + str(answer())

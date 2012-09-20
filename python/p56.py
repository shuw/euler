maxSum = 0
for a in range(1,100):
    for b in range(1,100):
        ab = a**b
        s = 0
        for d in str(ab):
            s += int(d)
        if s > maxSum:
            maxSum = s
            print str(maxSum) + ' digits: ' + str(ab)
            

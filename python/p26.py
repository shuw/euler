


def findCycleLength(n):
    d = 1
    count = 0

    # ignore initial zeros
    while d < n: d *= 10

    remainderMap = {}
    
    while True:
        if d == 0:
            return None #no cycles
        if d < n:
            d *= 10

        digit = d / n
        
        d = d % n            

        lastSeenCount = remainderMap.get(d)
        if lastSeenCount == None:
            remainderMap[d] = count
        else:
            return count - lastSeenCount

        # print digit # print cycles

        count += 1
            

maxLength = 0
for n in range(1, 1000):
    length = findCycleLength(n)
    if length != None and length > maxLength:
        maxLength = length
        print str(n) + " length: " + str(length)

import copy

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# digits = [0, 1, 2, 3]

count = 0

def solve(digits, path, depth):
    global count
    
    if depth == 0:
        count += 1
        if count == 1000000:
            print str(path) + " count: " + str(count)        
        return

    for d in digits:
        path2 = copy.copy(path)
        path2.append(d)

        digits2 = copy.copy(digits)
        digits2.remove(d)

        solve(digits2, path2, depth - 1)

print 'started'

solve(digits, [], len(digits))

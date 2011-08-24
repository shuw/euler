
prev = 0
current = 1

count = 2
while True:
    temp = current
    current = prev + current
    prev = temp

    length = len(str(current))
    print length

    if (length >= 1000):
        print count
        break;

    count += 1

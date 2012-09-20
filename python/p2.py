prev = 0
current = 1

sum = 0;
for i in range(100):
    temp = current;
    current = prev + current;
    prev = temp;

    if (current > 4000000):
        break;
    
    if (current % 2 == 0):
        sum += current

print sum

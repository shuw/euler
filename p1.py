prev = 0
current = 1

for i in range(400):
    temp = current;
    current = prev + current;
    prev = temp;
    
    print current;

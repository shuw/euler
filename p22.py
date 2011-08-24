execfile("d:/code/projectEuler/names.py")

names.sort()

answer = 0
i = 1
for name in names:
    sum = 0
    for digit in name:
        sum += ord(digit) - 64

    
    answer += sum * i
    i += 1

print answer

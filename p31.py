coins = [200, 100, 50, 20, 10, 5, 2, 1]


def make2pounds(value, pos):    
    if value == 200:        
        return 1
    elif value > 200:
        return 0

    combinations = 0
    for i in range(pos, len(coins)):
        v = value + coins[i]
        combinations += make2pounds(v, i)
        
    return combinations
    
print make2pounds(0, 0)

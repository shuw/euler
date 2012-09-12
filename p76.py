def solve(N):
    """Dynamic Programming approach solution to project Euler 76"""
    # initial 1 indicates that a number can always be a sum of itself
    ways = [1] + [0] * N
    for component in range(1, N):
        for index in range(N + 1 - component):
            ways[index + component] += ways[index]

    return ways[-1]

print(solve(100))

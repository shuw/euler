import math


def sqrt(n):
    estimate = n / 2.0
    iterations = 0

    while True:
        iterations += 1
        bound = n / estimate
        if math.fabs((bound - estimate) / estimate) <= 0.000000001:
            return (estimate, iterations)

        estimate = (estimate + bound) / 2.0


def test(n):
    expected = math.sqrt(n)
    actual, iterations = sqrt(n)
    error = math.fabs(expected - actual)

    if expected:
        accuracy = (expected - error) / expected
    else:
        accuracy = 'n/a'

    print("accuracy: %s, expected: %s, actual: %s, iterations: %s" % \
        (accuracy, expected, actual, iterations))

if __name__ == '__main__':
    test(1)
    test(4)
    test(61234234423455)
    test(232379238546328645235)

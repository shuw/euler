import math


def sqrt(n):
    lower_estimate = 0
    upper_estimate = n
    margin = n * 0.00000001

    estimate = upper_estimate / 2
    iterations = 0

    while True:
        iterations += 1
        error = (estimate * estimate) - n
        if math.fabs(error) < margin:
            return (estimate, iterations)

        # too big
        if error > 0:
            upper_estimate = estimate
        else:
            lower_estimate = estimate

        estimate = (upper_estimate + lower_estimate) / 2.0


def test(n):
    expected = math.sqrt(n)
    actual, iterations = sqrt(n)
    error = math.fabs(expected - actual)
    accuracy = (expected - error) / expected

    print("expected: %s, actual: %s, accuracy: %s, iterations: %s" % \
        (expected, actual, accuracy, iterations))

if __name__ == '__main__':
    test(61234234423455)

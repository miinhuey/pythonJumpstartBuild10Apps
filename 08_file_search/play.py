# 5! = 120:
#
# 5 * 4 * 3 * 2 * 1


def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


print("5!={:,}, 3!={:,}, 11!={:,}".format(
    factorial(5),
    factorial(3),
    factorial(11),
))


def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        nums.append(current)

    return nums


print('via lists')
for n in fibonacci(100):
    print(n, end=', ')

print()


def fibonacci_co(limit):
    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        yield current


print('with yield')
for n in fibonacci_co(100):
    print(n, end=', ')
def fib(n):
    a, b = 0, 1
    result = []
    for index in range(n):
        result.append(a)
        a, b = b, b + a

    return result

def binary_search(x, xs):
    left = 0
    right = len(xs) - 1

    while left <= right:
        midddle = (left + right) // 2
        y = xs[midddle]
        if x == y:
            return (True, midddle)
        elif x < y:
            right = midddle - 1
        elif x > y:
            left = midddle + 1

    return False


print(binary_search(2, [1, 2, 3]))

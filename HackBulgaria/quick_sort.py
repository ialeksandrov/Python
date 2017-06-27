def quick_sort(xs):
    if len(xs) <= 1:
        return xs

    pivot = xs[0]
    lower = [x for x in xs if x < pivot]
    grater = [x for x in xs if x > pivot]
    pivots = [x for x in xs if x == pivot]
    return quick_sort(lower) + pivots + quick_sort(grater)

print(quick_sort([-10, 16, 20, 30, -20, 5, -100]))


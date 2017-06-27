from math import log


def count(n):
    counter = 0
    n = 10 ** 10
    while n >= 1:
        n = n // 2
        counter += 1

    return counter

def log(n):
bla = log(10 ** 10, 2)
print(bla)

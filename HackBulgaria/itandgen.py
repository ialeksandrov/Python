from functools import reduce


def chain(iterable_one, iterabe_two):
    yield from iterable_one
    yield from iterabe_two

print(list(chain(range(0, 4), range(4, 8))))


def compress(iterable, mask):
    return (i[0] for i in zip(iterable, mask) if all(i))

print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))


def cycle(iterable):
    while True:
        yield from iterable

endless = cycle(range(0, 10))
for item in endless:
    print(item)




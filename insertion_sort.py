def insertion_sort(list):
    for index in range(1, len(list)):
        value = list[index]
        i = index - 1
        while i >= 0 and (value < list[i]):
                list[i + 1] = list[i] # shift number in slot i right to slot i + 1
                list[i] = value # shift value lef into slot i
                i = i - 1

a = [4, 5, 7, 10, 9, 2, 1, 3]
insertion_sort(a)
print a

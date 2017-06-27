def birthday_ranges(birthdays, ranges):
    result = []
    count = 0
    for range in ranges:
        for birthday in birthdays:
            if range[0] <= birthday and range[1] >= birthday:
                count += 1
        result.append(count)
        count = 0
    return result

print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))

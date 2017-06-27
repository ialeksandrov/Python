def counting_sort(nums, upper_limit=None):
    if upper_limit is None:
        upper_limit = max(nums)

    result = []
    counts = [0] * (upper_limit + 1)

    for n in nums:
        counts[n] += 1

    for i in range(len(counts)):
        count = counts[i]
        result.extend([i] * count)

    return result

print(counting_sort([0, 1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1]))

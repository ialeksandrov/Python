from copy import deepcopy


class SlowSorts:
    @staticmethod
    def bubble_sort(xs):
        """Returns a newly sorted list"""
        results = deepcopy(xs)
        n = len(results)
        swapped = True
        while swapped:
            swapped = False
            for i in range(0, n - 1):
                if results[i] > results[i + 1]:
                    temp = results[i]
                    results[i] = results[i + 1]
                    results[i + 1] = temp
                    swapped = True
        return results

    @staticmethod
    def selection_sort(xs):
        """Returns a newly sorted list"""
        results = []
        xs_copy = deepcopy(xs)
        for i in range(len(xs)):
            x = min(xs_copy)
            results.append(x)
            xs_copy.remove(x)

        return results

# print(SlowSorts.bubble_sort([0, 1, 2, 3, -1, -2]))
# print(SlowSorts.selection_sort([0, 1, 2, 3, -1, -2]))



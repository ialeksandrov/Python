def cmp(x, y):
    if x < y:
        return -1

    if x == y:
        return 0

    return 1


class Node:
    """
    Node , used for implementation of Binary Search Tree
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.left = None
        self.right = None


class SortedMap:
    """
    This is a key-value container that keeps a sorted represnetation
    Sorting is done using the comparator function passed to __init__
    If no comparator is passed, natural order of keys is used:
    k1 <> k2
    """
    def __init__(self, comparator=None):
        if comparator is None:
            comparator = cmp

        self.__comparator = comparator
        self.__root = None

    def __repr__(self):
        return repr(self__dict__)

    def add(self, key, value):
        """
        Adds a new key-value pair
        If the key is already existing - override it
        """
        self.dict[key] = value
        print(self.dict)

    def get(self, key, default=None):
        """
        Should return the corresponding value to key
        Returns default otherwise
        """

    def __contains__(self, key):
        """
        Usage: key in map
        """
        if key in self.dict:
            return True
        else:
            return False

    def __iter__(self):
        result = []

        """
        Code here that populates result with values
        """

        return iter(result)

storage = SortedMap()
storage.add('b', 5)
storage.add('a', 4)
print(storage)

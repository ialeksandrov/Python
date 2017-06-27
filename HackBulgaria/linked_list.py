class Node:
    def __init__(self, value, next=None):
        self.value = value

        if next is not None and \
                not isinstance(next, Node):
            raise TypeError('next_node should be instance of Node')

        self.next = next

    def has_next(self):
        return self.next is not None

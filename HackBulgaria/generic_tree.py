from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        if not isinstance(node, Node):
            raise ValueError('node should be Node')

        self.children.append(node)

    def __str__(self):
        values = {
            'value': self.value
            'children': ', '.join(str([(child) for child in self.children])
        }
        return "node: {value}, children: {children}" \
                .format(**values)


class Tree:
    def __init__(self, *, root):
        """
            When we are creating a new tree, we must always have a root element.
            For example:
            tree = Tree(root=5)
        """
        self._root = Node(root)

    def __find_node_by_value(self, value):
        q = deque()
        q.append(self__root, 1)

        while len(q) != 0:
            node, level = q.popleft()

            if node.value == value:
                return node

            for child in node.children:
                q.append(child, level + 1)

    def add(self, *, value, parent):
        """
            When we are adding new element to our tree, we must specify the parent:
            tree = Tree(root=5)
            tree.add(value=4, parent=5)
            tree.add(value=3, parent=5)
            tree.add(value=2, parent=4)

            This will make the following tree:

                5
               / \
              4   3
             /
            2
        """
        parent_node = self.__find_node_by_value(parent)
        parent_node.add_child(Node(value))
    def find(self, x):
        """
            Returns True or False if Node with value x is present in the tree
        """
        node = self.__find_node_by_value(x)

        return node is not None

    def bfs_from_root(self):
        """
            Makes a Breadth-First-Search Algorithm from root
            Returns a list of tuples in the following format:
            [(tree_level, (node1_on_that_level, node2_on_that_level, ...)),
             (tree_level + 1, (node1_on_that_level, node2_on_that_level, ...))]

            If we take the tree from the add example, the result will look like that:

            [(1, (5, )),
             (2, (4, 3)),
             (3, (2, ))]

             We count our levels from 1.
        """


t = Tree(root=5)
print(t)

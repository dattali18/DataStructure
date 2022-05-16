class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None

    def _in_order_rec(self):
        if self.right:
            self.right._in_order_rec()
        print(self)
        if self.left:
            self.left._in_order_rec()

    def __repr__(self):
        return f"{self.data = }"


class BST:
    root: Node

    def __init__(self, data=None):
        self.root = Node(data=data)

    def insert(self, data):
        new_node = Node(data)
        # ptr1 = None
        ptr2 = None
        # if the tree is empty
        if self.root.data is None:
            self.root.data = data
        else:
            ptr1 = self.root
            while ptr1:
                ptr2 = ptr1
                if new_node.data > ptr2.data:
                    ptr1 = ptr1.left
                else:
                    ptr1 = ptr1.right

            new_node.parent = ptr2

            if new_node.data > ptr2.data:
                ptr2.left = new_node
            else:
                ptr2.right = new_node

    def search(self, data):
        ptr = self.root
        while ptr:
            if ptr.data == data:
                return ptr
            elif data < ptr.data:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return None

    def minimum(self):
        return BST._minimum_node(self.root)

    def maximum(self):
        return BST._maximum_node(self.root)

    def in_order(self):
        self.root._in_order_rec()

    # static methods
    @staticmethod
    def _minimum_node(node: Node):
        ptr = node
        while ptr.left:
            ptr = ptr.left
        return ptr

    @staticmethod
    def _maximum_node(node: Node):
        ptr = node
        while ptr.right:
            ptr = ptr.right
        return ptr

    @staticmethod
    def _successor(node: Node) -> Node:
        """
        :rtype: Node
        """
        if node.right:
            return BST._minimum_node(node.right)
        ptr1 = node.parent
        while ptr1 and node == ptr1.right:
            node = ptr1
            ptr1 = node.parent
        return ptr1

    @staticmethod
    def _predecessor(node: Node) -> Node:
        """
        :rtype: Node
        """
        if node.left:
            return BST._maximum_node(node.left)
        ptr1 = node.parent
        while ptr1 and node == ptr1.left:
            node = ptr1
            ptr1 = node.parent
        return ptr1


def create_BST(n=100):
    import random
    tree = BST()
    for i in range(n):
        tree.insert(random.randint(i, i * i))
    return tree


def main():
    tree = create_BST(10)
    node1 = tree.root.left.left
    pre = tree._predecessor(node1)
    print(node1)
    print(pre)
    print(tree._successor(pre))


if __name__ == '__main__':
    main()

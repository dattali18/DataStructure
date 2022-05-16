class Leaf:
    def __init__(self, data=None):
        self.right = None
        self.left = None
        self.data = data

    def pre_order_rec(self):
        print(self.data)
        if self.left:
            self.left.pre_order_rec()
        if self.right:
            self.right.pre_order_rec()

    def in_order_rec(self):
        if self.left:
            self.left.pre_order_rec()
        print(self.data)
        if self.right:
            self.right.pre_order_rec()

    def post_order_rec(self):
        if self.left:
            self.left.pre_order_rec()
        if self.right:
            self.right.pre_order_rec()
        print(self.data)

    def __repr__(self):
        return f"{self.data = }\n{self.right = }\n{self.left = }"


# the class Binary tree is a BST
class BinaryTree:
    def __init__(self, data=None):
        self.root = Leaf(data)

    def pre_order(self):
        self.root.pre_order_rec()

    def in_order(self):
        self.root.in_order_rec()

    def post_order(self):
        self.root.post_order_rec()

    def insert(self, data):
        if self.root.data is None:
            self.root.data = data
            return self.root
        if self.root.data > data:
            self.root.left = self.root.left.insert(data)
        else:
            self.root.right = self.root.right.insert(data)
        return self


def main():
    tree = BinaryTree(1)
    tree.insert(2)
    tree.insert(4)
    tree.insert(-1)
    tree.insert(4)
    tree.in_order()


if __name__ == '__main__':
    main()

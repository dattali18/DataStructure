from typing import Optional, Any


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.height = 1


class AVLTree:
    root: Node

    def __init__(self):
        self.root = None

    def insert(self, root: Node, key):
        if root is None:
            return Node(key)
        elif key <= root.value:
            root.left = self.insert(root.left, key)
        elif key > root.value:
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)
        if balance > 1 and root.left.value > key:
            return self.rotateRight(root)
        if balance < 1 and root.right.value < key:
            return self.rotateLeft(root)
        if balance > 1 and root.left.value < key:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        if balance < 1 and root.right.value > key:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
        return root

    def delete(self, node: Node, key):
        if node is None:
            return node
        elif key < node.value:
            node.left = self.delete(node.left, key)
        elif key > node.value:
            node.right = self.delete(node.right, key)
        else:
            if node.left is None:
                lt = node.right
                node = None
                return lt
            elif node.right is None:
                lt = node.left
                node = None
                return lt
            rgt = self.maximum(node.right)
            node.value = rgt.value

    @staticmethod
    def height(node: Node):
        if node is None:
            return 0
        return node.height

    def balance(self, node: Node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def maximum(self, node: Node) -> Optional[Node]:
        if node is None or node.left is None:
            return node
        return self.maximum(node.left)

    def rotateRight(self, node: Node):
        a: Node
        b: Node
        a = node.left
        b = a.right
        a.right = node
        node.left = b
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    def rotateLeft(self, node: Node):
        a: Node
        b: Node
        a = node.left
        b = a.right
        a.left = node
        node.right = b
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

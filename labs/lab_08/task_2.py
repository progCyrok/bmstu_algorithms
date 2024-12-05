class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def _getHeight(self, node):
        if not node:
            return 0
        return node.height

    def _getBalance(self, node):
        if not node:
            return 0
        return self._getHeight(node.left) - self._getHeight(node.right)

    def _rotateRight(self, z):
        y = z.left
        T2 = y.right

        y.right = z
        z.left = T2

        z.height = 1 + max(self._getHeight(z.left), self._getHeight(z.right))
        y.height = 1 + max(self._getHeight(y.left), self._getHeight(y.right))

        return y

    def _rotateLeft(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._getHeight(z.left), self._getHeight(z.right))
        y.height = 1 + max(self._getHeight(y.left), self._getHeight(y.right))

        return y

    def _insertRecursive(self, node, key):
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self._insertRecursive(node.left, key)
        else:
            node.right = self._insertRecursive(node.right, key)

        node.height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))

        balance = self._getBalance(node)

        if balance > 1 and key < node.left.key:
            return self._rotateRight(node)

        if balance < -1 and key > node.right.key:
            return self._rotateLeft(node)

        if balance > 1 and key > node.left.key:
            node.left = self._rotateLeft(node.left)
            return self._rotateRight(node)

        if balance < -1 and key < node.right.key:
            node.right = self._rotateRight(node.right)
            return self._rotateLeft(node)

        return node

    def insert(self, key):
        self.root = self._insertRecursive(self.root, key)


    def _findMinNode(self, node):
        if node is None or node.left is None:
            return node
        return self._findMinNode(node.left)


    def _deleteRecursive(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._deleteRecursive(node.left, key)
        elif key > node.key:
            node.right = self._deleteRecursive(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self._findMinNode(node.right)
            node.key = temp.key
            node.right = self._deleteRecursive(node.right, temp.key)

        if node is None:
            return node

        node.height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))

        balance = self._getBalance(node)

        if balance > 1 and self._getBalance(node.left) >= 0:
            return self._rotateRight(node)

        if balance < -1 and self._getBalance(node.right) <= 0:
            return self._rotateLeft(node)

        if balance > 1 and self._getBalance(node.left) < 0:
            node.left = self._rotateLeft(node.left)
            return self._rotateRight(node)

        if balance < -1 and self._getBalance(node.right) > 0:
            node.right = self._rotateRight(node.right)
            return self._rotateLeft(node)

        return node

    def delete(self, key):
        self.root = self._deleteRecursive(self.root, key)

    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return True
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

    def print_tree(self, node, level=0):
        if node is None:
            return

        self.print_tree(node.right, level + 1)
        print("  " * level + str(node.key))
        self.print_tree(node.left, level + 1)


myTree = AVLTree()

myTree.insert(10)
myTree.insert(20)
myTree.insert(30)
myTree.insert(40)
myTree.insert(50)
myTree.insert(25)

print("Дерево AVL")
myTree.print_tree(myTree.root)

print("Порядок дерева AVL")
myTree.inorder_traversal(myTree.root)


print("Поиск 25:", myTree.search(25))  # True
print("Поиск 100:", myTree.search(100)) # False

myTree.delete(20)

print("Обход по порядку после удаления 20:")
myTree.inorder_traversal(myTree.root)

print("Дерево AVL")
myTree.print_tree(myTree.root)

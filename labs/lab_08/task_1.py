class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(node.left, data)
        return self._search_recursive(node.right, data)

    def delete(self, data):
        if self.is_empty():
            print("Дерево пустое. Удаление невозможно.")
            return

        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.data = min_node.data
                node.right = self._delete_recursive(node.right, min_node.data)

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)

    def print_tree(self):
        if self.is_empty():
            print("Дерево пустое")
            return
        self._print_tree_recursive(self.root, "", True)


    def _print_tree_recursive(self, node, indent, last):
        if node:
            print(indent, end="")
            if last:
                print("└──", end="")
                indent += "   "
            else:
                print("├──", end="")
                indent += "|  "

            print(node.data)
            self._print_tree_recursive(node.left, indent, False)
            self._print_tree_recursive(node.right, indent, True)

    def height(self):
        return self._height_rec(self.root)

    def _height_rec(self, node):
        if node is None:
            return -1
        return 1 + max(self._height_rec(node.left), self._height_rec(node.right))



# Тесты
bst = BinarySearchTree()

print("Проверка пустого дерева:", bst.is_empty())  # True

bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(14)
bst.insert(4)
bst.insert(7)
bst.insert(13)


print("Прямой обход:", bst.preorder_traversal())  # [8, 3, 1, 6, 4, 7, 10, 14, 13]
print("Симметричный обход:", bst.inorder_traversal())  # [1, 3, 4, 6, 7, 8, 10, 13, 14]
print("Обратный обход:", bst.postorder_traversal())  # [1, 4, 7, 6, 3, 13, 14, 10, 8]

print("Печать дерева:")
bst.print_tree()

print("Поиск значения 6:", bst.search(6).data if bst.search(6) else "Значение не найдено")  # 6
print("Поиск значения 15:", bst.search(15) if bst.search(15) else "Значение не найдено")  # Значение не найдено

print("Высота дерева:", bst.height())  # 4

bst.delete(8)
print("Дерево после удаления 8:")
bst.print_tree()
print("Симметричный обход после удаления 8:", bst.inorder_traversal()) # [1, 3, 4, 6, 7, 10, 13, 14]


bst.delete(1)
print("Дерево после удаления 1:")
bst.print_tree()
print("Симметричный обход после удаления 1:", bst.inorder_traversal()) # [3, 4, 6, 7, 10, 13, 14]
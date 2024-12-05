<!-- #region editable=true slideshow={"slide_type": ""} -->
## Лабораторная работа № 8 (Binary Search Tree)
***Выполнил***: Камалов Ринат,  ***Группа***: ИУ10-36

### **Цель работы**
Изучение структуры данных «Двоичное дерево поиска», а также основных операций над ним.

### **Задание №1**
**1.** Реализовать программу, выполняющую стандартный набор операций над  двоичным деревом поиска:
- формирование бинарного дерева;
- обход (прямой, симметричный, обратный) бинарного дерева;
- удаление заданной вершины из бинарного дерева;
- поиск заданной вершины в бинарном дереве (по значению);
- печать бинарного дерева на экран;
- проверка пустоты бинарного дерева;
- определение высоты бинарного дерева.


```python
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

```

### **Задание №2**
**2.** Реализовать самобалансирующееся дерево (AVL-дерево для четных вариантов, красно-черное дерево для нечетных вариантов)


```python
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


```


### **Задание №3**
### **Индивидуальное задание**
Написать функцию, которая определяет, является ли бинарное дерево симметричным.


```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_symmetric(root):

    if root is None:
        return True

    def check(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.data != right.data:
            return False
        return check(left.left, right.right) and check(left.right, right.left)

    return check(root.left, root.right)


# Пример использования:
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

print(f"Дерево симметрично: {is_symmetric(root)}")  # True


root2 = Node(1)
root2.left = Node(2)
root2.right = Node(2)
root2.left.right = Node(3)
root2.right.left = Node(4)

print(f"Дерево симметрично: {is_symmetric(root2)}")  #  False



```


### **Контрольные вопросы**

1. **С чем связана популярность использования деревьев в программировании?**  
   Деревья популярны из-за их эффективности в организациях данных. Они обеспечивают быстрый доступ, вставку, удаление и поиск элементов, что делает их полезными для баз данных, системных приложений, графов и индексов.

2. **Можно ли список отнести к деревьям? Ответ обоснуйте.**  
   Список не является деревом, так как он имеет линейную структуру, где каждый элемент связан только с одним соседом. Дерево — это иерархическая структура, где у одного узла может быть несколько потомков.

3. **Какие данные содержат адресные поля элемента бинарного дерева?**  
   Адресные поля содержат ссылки на левого и правого потомка, а также на родительский узел (в некоторых реализациях).

4. **Что такое дерево, двоичное дерево, поддерево?**  
   - **Дерево** — иерархическая структура данных с корнем и узлами, связанными ребрами.  
   - **Двоичное дерево** — дерево, где каждый узел имеет не более двух потомков.  
   - **Поддерево** — часть дерева, представляющая собой самостоятельное дерево, начиная с определенного узла.

5. **Как рекурсивно определяется дерево?**  
   Дерево состоит из корня и набора поддеревьев, которые также являются деревьями. Базовый случай: пустое дерево.

6. **Какие основные понятия связываются с деревьями?**  
   Корень, узел, лист, высота, глубина, поддерево, родители, потомки, степень узла.

7. **Какие основные операции характерны при использовании деревьев?**  
   Обход (прямой, симметричный, обратный), поиск, добавление, удаление, балансировка.

8. **Как программно реализуется алгоритм операции обхода дерева?**  
   Обход дерева реализуется с помощью рекурсивных функций или стека. Например:  
   ```python
   def inorder_traversal(node):
       if node:
           inorder_traversal(node.left)
           print(node.key)
           inorder_traversal(node.right)
   ```

9. **Как программно реализуется алгоритм операции добавления элемента в дерево?**  
   Например, для бинарного дерева поиска:  
   ```python
   def insert(node, key):
       if not node:
           return Node(key)
       if key < node.key:
           node.left = insert(node.left, key)
       else:
           node.right = insert(node.right, key)
       return node
   ```

10. **Как программно реализуется алгоритм операции удаления элемента из дерева?**  
   В случае бинарного дерева:  
      * Найти узел.  
      * Если у узла 0 или 1 потомок — удалить и заменить.  
      * Если 2 потомка — найти преемника (минимальный элемент правого поддерева), заменить и удалить.  

   Пример:  
   ```python
   def delete(node, key):
       if not node:
           return node
       if key < node.key:
           node.left = delete(node.left, key)
       elif key > node.key:
           node.right = delete(node.right, key)
       else:
           if not node.left:
               return node.right
           if not node.right:
               return node.left
           temp = find_min(node.right)
           node.key = temp.key
           node.right = delete(node.right, temp.key)
       return node
   ```

11. **Как программно реализуется алгоритм операции поиска элемента в дереве?**  
   Для бинарного дерева поиска:  
   ```python
   def search(node, key):
       if not node or node.key == key:
           return node
       if key < node.key:
           return search(node.left, key)
       return search(node.right, key)
   ```

12. **Что такое самобалансирующееся дерево?**  
   Это дерево, которое автоматически поддерживает свою высоту минимально возможной после операций вставки и удаления, обеспечивая эффективность.

13. **Как определяется количество узлов в самобалансирующемся дереве?**  
   Максимальное количество узлов при высоте `h` соответствует \(2^h - 1\), минимальное — для конкретной структуры (например, AVL или красно-черных деревьев).

14. **Как происходит добавление элемента в самобалансирующееся дерево?**  
   Добавление выполняется аналогично бинарному дереву, но с последующей балансировкой (например, с помощью поворотов или перекраски).

15. **Как происходит удаление элемента из самобалансирующееся дерево?**  
   Удаление включает поиск элемента, удаление по правилам бинарного дерева и последующую балансировку.

16. **Особенности красно-черных деревьев.**  
   - Каждый узел окрашен в красный или черный цвет.  
   - Корень всегда черный.  
   - Красный узел не может иметь красных потомков.  
   - Все пути от узла до листа содержат одинаковое количество черных узлов.  

17. **Особенности АВЛ деревьев.**  
   - Высота левого и правого поддеревьев для любого узла отличается не более чем на 1.  
   - Обеспечивается балансировка после вставки или удаления.  
   - Подходит для частого поиска.

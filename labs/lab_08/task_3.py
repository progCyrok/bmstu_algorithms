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


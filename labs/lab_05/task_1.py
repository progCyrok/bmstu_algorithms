class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        new_node = Node(key, value)

        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next is not None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            current.next = new_node

    def search(self, key):
        index = self.hash(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self.hash(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next

    def print_table(self):
        for index, node in enumerate(self.table):
            if node is not None:
                print(f"Index {index}: ", end='')
                current = node
                while current is not None:
                    print(f"({current.key}: {current.value})", end=' -> ')
                    current = current.next
                print("None")
            else:
                print(f"Index {index}: None")

hash_table = HashTable()

hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("orange", 3)
hash_table.insert("grape", 4)

print("Содержимое хеш-таблицы:")
hash_table.print_table()

print("\nПоиск 'banana':", hash_table.search("banana"))

hash_table.delete("banana")
print("\nПосле удаления 'banana':")
hash_table.print_table()

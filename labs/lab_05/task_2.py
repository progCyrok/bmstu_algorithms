class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.deleted = object()

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        original_index = index

        while self.table[index] is not None and self.table[index] != self.deleted:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size

            if index == original_index:
                raise Exception("Hash table is full")

        self.table[index] = (key, value)

    def search(self, key):

        index = self.hash(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index] != self.deleted and self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size

            if index == original_index:
                break

        return None

    def delete(self, key):
        index = self.hash(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index] != self.deleted and self.table[index][0] == key:
                self.table[index] = self.deleted
                return
            index = (index + 1) % self.size

            if index == original_index:
                break

    def print_table(self):
        for index, item in enumerate(self.table):
            if item is None:
                print(f"Index {index}: None")
            elif item is self.deleted:
                print(f"Index {index}: Deleted")
            else:
                print(f"Index {index}: ({item[0]}: {item[1]})")


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

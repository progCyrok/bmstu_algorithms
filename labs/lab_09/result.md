## Лабораторная работа № 9 (Криптоалгоритмы)
***Выполнил***: Камалов Ринат,  ***Группа***: ИУ10-36

### **Цель работы**
Изучение структуры данных «Двоичное дерево поиска», а также основных операций над ним.

### **Задание №1**
1. Реализовать программу, выполняющую шифрование и расшифровку текста двумя разными методами. 
Для методов, требующих ключа определенного вида, например для перестановок, ключ должен формироваться на основании одного произвольного ключа, задаваемого пользователем. 
Пример ключа: фф12К52. Зашифрованный и дешифрованный тексты должны быть идентичными.

### **Шифр Хилла**
```python
import numpy as np
import math


def generate_hill_matrix(key_str):
    n = 2
    key_bytes = key_str.encode('utf-8')
    key_len = len(key_bytes)
    if key_len < n * n:
        key_bytes = key_bytes * (n * n // key_len + 1)

    for i in range(10):
        key_nums = [int(key_bytes[(i + j) % len(key_bytes)]) for j in range(n * n)]
        matrix = np.array(key_nums).reshape((n, n))
        if math.gcd(round(np.linalg.det(matrix)) % 256, 256) == 1:
            return matrix
    print("Не удалось сгенерировать обратимую матрицу. Попробуйте другой ключ.")
    return None


def matrix_mod_inverse(matrix, modulus):
    det = round(np.linalg.det(matrix)) % modulus
    if math.gcd(det, modulus) != 1:
        raise ValueError("Определитель не взаимно прост с модулем, матрица необратима!")

    det_inv = pow(det, -1, modulus)
    adj = np.round(np.linalg.det(matrix) * np.linalg.inv(matrix)).astype(int)
    return (adj * det_inv) % modulus


def text_to_matrix(text):
    n = 2
    nums = [ord(c) for c in text]

    padding_len = (n - len(nums) % n) % n
    nums.extend([0] * padding_len)

    return np.array(nums).reshape(-1, n)


def matrix_to_text(matrix):
    return ''.join(chr(i) for row in matrix for i in row)


def encrypt_hill(text, key_matrix):
    text_matrix = text_to_matrix(text)
    encrypted_matrix = (text_matrix @ key_matrix) % 256
    return matrix_to_text(encrypted_matrix)


def decrypt_hill(encrypted_text, key_matrix):
    encrypted_matrix = text_to_matrix(encrypted_text)
    inv_key_matrix = matrix_mod_inverse(key_matrix, 256)
    decrypted_matrix = (encrypted_matrix @ inv_key_matrix) % 256
    return matrix_to_text(decrypted_matrix)


if __name__ == "__main__":
    user_key = input("Введите произвольный ключ: ")
    key_matrix = generate_hill_matrix(user_key)
    if key_matrix is None:
        exit()

    text = input("Введите текст для шифрования: ")

    encrypted_text = encrypt_hill(text, key_matrix)
    print("Зашифрованный текст:", encrypted_text)

    decrypted_text = decrypt_hill(encrypted_text, key_matrix)[:-1]
    print("Расшифрованный текст:", decrypted_text)

    if text == decrypted_text:
        print("Шифрование и расшифрование прошли успешно")
    else:
        print("Ошибка: расшифрованный текст не совпадает с оригинальным!")

# Введите произвольный ключ: dsf22h3h
# Введите текст для шифрования: hello
# Зашифрованный текст: ,´d
# Расшифрованный текст: hello
# Шифрование и расшифрование прошли успешно

```

### **Криптосистема Крамера – Шоупа**

```python
import random
from hashlib import sha256

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def power(base, exp, modulus):
    result = 1
    base = base % modulus
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exp //= 2
    return result


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


# Генерация ключей
def generate_keys(key_size=1024):
    p = generate_large_prime(key_size // 2)
    q = generate_large_prime(key_size // 2)
    n = p * q

    g = find_generator(n)

    x1 = random.randint(1, n - 1)
    x2 = random.randint(1, n - 1)
    y1 = random.randint(1, n - 1)
    y2 = random.randint(1, n - 1)
    z = random.randint(1, n - 1)

    c = power(g, x1, n)
    d = power(g, x2, n)
    h = power(g, z, n)
    u = (power(g, y1, n) * power(h, y2, n)) % n

    public_key = (n, g, c, d, u, h)
    private_key = (x1, x2, y1, y2, z)

    return public_key, private_key


def generate_large_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << (bits - 1)) | 1
        if is_prime(num):
            return num


def is_prime(num, k=5):
    if num <= 1: return False
    if num <= 3: return True
    if num % 2 == 0: return False

    r, s = num - 1, 0
    while r % 2 == 0:
        r //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, num - 2)
        x = power(a, r, num)
        if x == 1 or x == num - 1: continue

        for _ in range(s - 1):
            x = power(x, 2, num)
            if x == num - 1: break
        else:
            return False
    return True


def find_generator(n):
    for i in range(2, n):
        if gcd(i, n) == 1:
            return i
    return 2


# Шифрование
def encrypt(public_key, message):
    n, g, c, d, u, h = public_key
    r = random.randint(1, n - 1)

    v = power(g, r, n)
    e = power(u, r, n)

    m_int = int.from_bytes(message.encode(), byteorder='big')
    w = (m_int * power(h, r, n)) % n

    a_hash = hash_message((v, w), n)
    x = (power(c, r, n) * power(d, r * a_hash, n)) % n

    ciphertext = (v, w, x)
    return ciphertext


# Дешифрование
def decrypt(public_key, private_key, ciphertext):
    n, g, c, d, u, h = public_key
    x1, x2, y1, y2, z = private_key

    v, w, x = ciphertext

    a_hash = hash_message((v, w), n)
    check = (power(v, x1, n) * power(power(v, x2, n), a_hash, n)) % n

    if check != x:
        raise ValueError("Неверный шифротекст!")

    m_int = (w * mod_inverse(power(v, z, n), n)) % n

    return m_int.to_bytes((m_int.bit_length() + 7) // 8, byteorder='big').decode()


def hash_message(message, n):
    concat_str = str(message[0]) + str(message[1])
    hash_str = sha256(concat_str.encode()).hexdigest()
    return int(hash_str, 16) % n


if __name__ == "__main__":
    public_key, private_key = generate_keys(1024)

    message = input("Введите текст для шифровки: ")
    print(f"Изначальное сообщение: {message}")

    # Шифрование
    ciphertext = encrypt(public_key, message)
    print(f"Зашифрованное сообщение: {ciphertext}")

    # Дешифрование
    try:
        decrypted_message = decrypt(public_key, private_key, ciphertext)
        print(f"Дешифрованное сообщение: {decrypted_message}")
    except ValueError as e:
        print(f"Ошибка при дешифровании: {e}")


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

# Введите текст для шифровки: hello
# Изначальное сообщение: hello
# Зашифрованное сообщение: (43058989597685896862201535077284569875886100107283379411140885788040332853836093338049770157299629376378001988774423845412270325690960558957189074336043714810638464180256387711909413956593965134144837087504738998056150210976207412621906248792753430435826437343133184044460473486027205163706531836787887304429, 40533528366980873886907385433784277735281551828052942109155024875728140123658436586674058570483507928779460692457942856339864126583989869615430500403600552286503760135660326087314131545342828182127417854014305516140770605957115664467166041622970277100083076081863604051761642761522761398916020759662560480805, 34764974056321698648544306456795989779878152890328820430487971834092145185605940721315063024654048563556782283869458093259425106372175892020937416141797097306803647727965660400366867480781085433352844573094835027022969238824464299496192903114042131816472889015215240651538711585562220915296015798899836042398)
# Дешифрованное сообщение: hello


```


### **Контрольные вопросы**

1) Что такое симметричные криптоалгоритмы?
Симметричные криптоалгоритмы используют один и тот же ключ как для шифрования, так и для расшифровки данных. Примеры: AES, DES, шифр Вернама.

2) Что такое асимметричные криптоалгоритмы?
Асимметричные криптоалгоритмы используют пару ключей: открытый для шифрования и закрытый для расшифровки. Примеры: RSA, алгоритм Эль-Гамаля.

3) Классификация симметричных криптоалгоритмов.
По типу данных: блочные, поточные.
По методу шифрования: подстановки, перестановки, комбинированные.
По типу ключей: фиксированный, динамический.

4) Классификация асимметричных криптоалгоритмов.
По области применения: шифрование, цифровая подпись, обмен ключами.
По математическим основам: алгоритмы на основе разложения на множители (RSA), алгоритмы на эллиптических кривых, алгоритмы на основе дискретного логарифма.

5) Обобщенная схема симметричной криптосистемы.
Сообщение шифруется с помощью симметричного ключа.
Ключ передаётся между сторонами защищённым каналом.
Получатель использует тот же ключ для расшифровки.

6) Блочные и поточные шифры.
Блочные шифры обрабатывают данные блоками фиксированной длины (например, AES). Поточные шифры работают с данными побитно или посимвольно (например, RC4).

7) Какие методы подстановки, используемые для шифрования, вы знаете?
Шифр Цезаря.
Шифр Виженера.
Шифр Вернама.
Шифр Атбаш.
8) Какие методы перестановки, используемые для шифрования, вы знаете?
Простая перестановка символов в тексте.
Перестановка по ключу (например, с использованием числовой последовательности).
9) Что понимается под шифрованием информации методом гаммирования?
Гаммирование — это метод шифрования, в котором к открытому тексту применяется побитовое или посимвольное сложение с ключевой последовательностью (гаммой).

10) Что называется ключом в криптосистеме?
Ключ — это уникальная информация (набор данных), используемая для шифрования и расшифровки сообщений.

11) Разовый блокнот.
Разовый блокнот — это шифр, использующий случайно сгенерированную гамму длиной, равной длине сообщения. Он абсолютно криптостойкий, если гамма используется только один раз.

12) Что такое криптостойкость системы?
Криптостойкость — это мера защищённости криптосистемы от взлома. Она зависит от сложности алгоритма, длины ключа и устойчивости к атакам.

13) Правила использования ключа.
Ключ должен быть случайным.
Должен передаваться по защищённому каналу.
Не использовать один ключ для разных сообщений.
Должен быть недоступен третьим лицам.
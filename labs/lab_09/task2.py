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

# Введите текст для шифровки: hello
# Изначальное сообщение: hello
# Зашифрованное сообщение: (43058989597685896862201535077284569875886100107283379411140885788040332853836093338049770157299629376378001988774423845412270325690960558957189074336043714810638464180256387711909413956593965134144837087504738998056150210976207412621906248792753430435826437343133184044460473486027205163706531836787887304429, 40533528366980873886907385433784277735281551828052942109155024875728140123658436586674058570483507928779460692457942856339864126583989869615430500403600552286503760135660326087314131545342828182127417854014305516140770605957115664467166041622970277100083076081863604051761642761522761398916020759662560480805, 34764974056321698648544306456795989779878152890328820430487971834092145185605940721315063024654048563556782283869458093259425106372175892020937416141797097306803647727965660400366867480781085433352844573094835027022969238824464299496192903114042131816472889015215240651538711585562220915296015798899836042398)
# Дешифрованное сообщение: hello
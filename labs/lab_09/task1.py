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
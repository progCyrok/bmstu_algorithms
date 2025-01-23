import numpy as np


def create_hill_key_matrix(key):
    # Приводим ключ к верхнему регистру и отфильтровываем не алфавитные символы
    key = ''.join(filter(str.isalpha, key.upper()))

    # Убираем дубликаты и заполняем матрицу
    key = list(dict.fromkeys(key))
    size = int(np.ceil(len(key) ** 0.5))  # Размер матрицы
    key_matrix = np.zeros((size, size), dtype=int)

    # Заполняем матрицу
    for i in range(size):
        for j in range(size):
            if i * size + j < len(key):
                key_matrix[i][j] = ord(key[i * size + j]) - ord('A')

    return key_matrix


def hill_encrypt(plain_text, key):
    key_matrix = create_hill_key_matrix(key)
    size = key_matrix.shape[0]

    # Приводим текст к верхнему регистру
    plain_text = ''.join(filter(str.isalpha, plain_text.upper()))

    # Заполняем текст в векторы
    while len(plain_text) % size != 0:
        plain_text += 'X'  # Добавляем 'X' для завершения

    plain_text_vectors = [ord(char) - ord('A') for char in plain_text]
    cipher_text = []

    # Шифруем текст
    for i in range(0, len(plain_text_vectors), size):
        vector = np.array(plain_text_vectors[i:i + size]).reshape(size, 1)
        cipher_vector = np.mod(np.dot(key_matrix, vector), 26)
        cipher_text.extend(cipher_vector.flatten().astype(int))

    # Преобразуем в символы
    return ''.join(chr(num + ord('A')) for num in cipher_text)


def hill_decrypt(cipher_text, key):
    key_matrix = create_hill_key_matrix(key)
    size = key_matrix.shape[0]

    # Находим обратную матрицу шифрования
    determinant = int(np.round(np.linalg.det(key_matrix))) % 26
    inverse_determinant = pow(determinant, -1, 26)
    adjugate_matrix = np.round(determinant * np.linalg.inv(key_matrix)).astype(int) % 26

    decrypt_matrix = (inverse_determinant * adjugate_matrix) % 26

    cipher_text_vectors = [ord(char) - ord('A') for char in cipher_text]
    decrypted_text = []

    for i in range(0, len(cipher_text_vectors), size):
        vector = np.array(cipher_text_vectors[i:i + size]).reshape(size, 1)
        decrypted_vector = np.mod(np.dot(decrypt_matrix, vector), 26)
        decrypted_text.extend(decrypted_vector.flatten().astype(int))

    return ''.join(chr(num + ord('A')) for num in decrypted_text)


# Пример использования
key = "фф12К52"
plain_text = "HELLOHILL"

cipher_text = hill_encrypt(plain_text, key)
print(f"Зашифрованный текст: {cipher_text}")

decrypted_text = hill_decrypt(cipher_text, key)
print(f"Расшифрованный текст: {decrypted_text}")

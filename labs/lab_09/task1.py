import numpy as np
from numpy.linalg import inv
from math import gcd


# Функция для получения алфавита и определения его размера
def prepare_alphabet():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alphabet, len(alphabet)


# Преобразование текста в числовой вид
def text_to_numbers(text, alphabet):
    return [alphabet.index(char) for char in text if char in alphabet]


# Преобразование чисел в текст
def numbers_to_text(numbers, alphabet):
    return ''.join(alphabet[i] for i in numbers)


# Создание ключевой матрицы
def generate_key_matrix(key):
    size = int(len(key) ** 0.5)  # размер матрицы
    key_numbers = [ord(char.upper()) - ord('A') for char in key if char.isalpha()]

    if len(key_numbers) < size ** 2:
        raise ValueError("Ключ недостаточно длинный для матрицы!")

    key_matrix = np.array(key_numbers)[:size ** 2].reshape(size, size)
    if np.linalg.det(key_matrix) % 26 == 0:
        raise ValueError("Определитель ключевой матрицы не может быть нулем по модулю 26.")

    return key_matrix


# Шифрование текста
def hill_encrypt(plain_text, key):
    alphabet, n = prepare_alphabet()
    key_matrix = generate_key_matrix(key)
    plain_numbers = text_to_numbers(plain_text.upper(), alphabet)

    # Дополняем текст до кратного размера матрицы
    while len(plain_numbers) % key_matrix.shape[0] != 0:
        plain_numbers.append(alphabet.index('X'))  # добавляем букву X в качестве заполнителя

    plain_array = np.array(plain_numbers).reshape(-1, key_matrix.shape[0])
    cipher_matrix = np.dot(plain_array, key_matrix) % 26
    cipher_numbers = cipher_matrix.flatten()

    return numbers_to_text(cipher_numbers, alphabet)


# Расшифровка текста
def hill_decrypt(cipher_text, key):
    alphabet, n = prepare_alphabet()
    key_matrix = generate_key_matrix(key)

    # Находим обратную матрицу
    key_matrix_inv = np.round(inv(key_matrix)).astype(int) % 26
    cipher_numbers = text_to_numbers(cipher_text, alphabet)
    cipher_array = np.array(cipher_numbers).reshape(-1, key_matrix.shape[0])
    plain_matrix = np.dot(cipher_array, key_matrix_inv) % 26
    plain_numbers = plain_matrix.flatten()

    return numbers_to_text(plain_numbers, alphabet)


# Пример использования
if __name__ == "__main__":
    key = input("Введите ключ (используя буквы): ")
    plaintext = input("Введите текст для шифрования: ")

    encrypted_text = hill_encrypt(plaintext, key)
    print(f"Зашифрованный текст: {encrypted_text}")

    decrypted_text = hill_decrypt(encrypted_text, key)
    print(f"Расшифрованный текст: {decrypted_text}")

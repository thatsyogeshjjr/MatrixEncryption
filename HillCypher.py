import numpy as np


def text_to_numbers(text):
    """Convert text to a list of numbers where 'A' is 0, 'B' is 1, ..., 'Z' is 25."""
    return [(ord(char) - ord('A')) for char in text.upper() if char.isalpha()]


def numbers_to_text(numbers):
    """Convert a list of numbers back to text where 0 is 'A', 1 is 'B', ..., 25 is 'Z'."""
    return ''.join([chr(num + ord('A')) for num in numbers])


def encrypt(plaintext, key_matrix):
    """Encrypt plaintext using Hill Cipher with the provided key matrix."""
    plaintext_numbers = text_to_numbers(plaintext)
    # Ensure the text length is even by padding if necessary
    if len(plaintext_numbers) % 2 != 0:
        plaintext_numbers.append(0)  # Padding with 'A' (0)

    # Reshape plaintext into a 2xN matrix for encryption
    plaintext_matrix = np.array(plaintext_numbers).reshape(-1, 2).T
    encrypted_matrix = np.dot(key_matrix, plaintext_matrix) % 26
    encrypted_text = numbers_to_text(encrypted_matrix.T.flatten())
    return encrypted_text


def decrypt(ciphertext, key_matrix):
    """Decrypt ciphertext using Hill Cipher with the provided key matrix."""
    ciphertext_numbers = text_to_numbers(ciphertext)
    # Reshape ciphertext into a 2xN matrix for decryption
    ciphertext_matrix = np.array(ciphertext_numbers).reshape(-1, 2).T

    try:
        # Calculate the inverse of the key matrix mod 26
        key_inverse = np.linalg.inv(key_matrix)
        det = int(round(np.linalg.det(key_matrix))) % 26
        det_inv = pow(det, -1, 26)  # Modular inverse of the determinant
        adjugate = np.round(key_inverse * det).astype(int) % 26
        key_matrix_inverse = (det_inv * adjugate) % 26
    except np.linalg.LinAlgError:
        print("The key matrix is not invertible.")
        return ""

    decrypted_matrix = np.dot(key_matrix_inverse, ciphertext_matrix) % 26
    decrypted_text = numbers_to_text(decrypted_matrix.T.flatten())
    return decrypted_text


# Sample 2x2 key matrix for encryption
key_matrix = np.array([[3, 3], [2, 5]])

# Input plaintext
plaintext = input("Enter the text to encrypt: ")
encrypted_text = encrypt(plaintext, key_matrix)
print("Encrypted text:", encrypted_text)

# Attempt decryption with user-provided key
try:
    key_input = input("key: ")
    # Convert key_input to a matrix assuming format: "a b;c d"
    key_elements = list(map(int, key_input.replace(';', ' ').split()))
    user_key_matrix = np.array(key_elements).reshape(2, 2)
    decrypted_text = decrypt(encrypted_text, user_key_matrix)
    print("Decrypted text:", decrypted_text)
except ValueError:
    print("Invalid key format. Please provide key as 'a b;c d'")

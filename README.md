# MatrixEncryption
_learning importance of matrices with a practical approach_

Matrices are a wonderful concept that can be a great tool in your skillset, some ways you can use these are:
* solving a system of equations (useful in things like finding solutions to equations of forces on a bridge)
* encryption
* AI and machine learning
* Linear algebra for optimization problems
* behavior of control systems are expressed in matrices
* Robot kinematics and dynamics
* more...

Here we explore one aspect of matrices' application. Transforming them from the good old topic in the textbook to something to look forward to. Sounds hard, but bear it with me.

## Encryption with matrices
#### 1. Matrix Multiplication and Key Transformation

- In a basic matrix encryption scheme, a plaintext message is first transformed into a numerical format and organized as a matrix. Then, this plaintext matrix is multiplied by an encryption key matrix to produce a ciphertext matrix. This matrix multiplication scrambles the plaintext based on the key, making it difficult to decode without the correct key.
- For decryption, the inverse of the key matrix (if it exists) is used to reverse the multiplication and recover the original plaintext.

#### 2. Hill Cipher

- The Hill Cipher is one of the most well-known encryption methods based on matrices. In this cipher, each letter in the plaintext is mapped to a number, and the plaintext is divided into blocks that match the dimensions of the key matrix.
- The encryption process involves multiplying each block by the key matrix. The key matrix must be invertible in the chosen modular arithmetic system (like modulo 26 for the alphabet).
- Decryption requires the inverse matrix of the key, allowing the recipient to recover the plaintext by reversing the matrix multiplication.

#### 3. Linear Transformations for Mixing Data

- In more advanced encryption algorithms, matrices are used to apply linear transformations that mix or "diffuse" the data. This is seen in algorithms like the Advanced Encryption Standard (AES), where linear transformations are applied to columns of the data matrix, enhancing the complexity and security of the encryption.
- These transformations make it so that small changes in plaintext result in significant changes in ciphertext, a desirable property known as the "avalanche effect."

#### 4. Generating Pseudorandom Number Matrices

- In symmetric key cryptography, matrices can generate pseudorandom numbers that serve as a keystream or as parts of the encryption key. The randomness achieved from matrix operations increases the encryption’s unpredictability, which is crucial for security.

#### 5. Error Detection and Correction

- Matrices are often involved in error detection and correction techniques within cryptographic protocols. The structure of matrices allows detection of data tampering or accidental alterations, adding an additional layer of security and data integrity.



## Story
The idea to explore matrices for it's practical application came from when i was listening to the second lecture in my first year Calculus and Matrices course. Looking at the grand topics of linear transformations, ranks and eigen values, my sleepy mind had to look for ways to make it interesting for me to look the board in awe instead of the watch on my wrist in a half asleep state.
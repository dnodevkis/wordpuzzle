import random
import string

def generate_random_letter(cyrillic=False):
    if cyrillic:
        return random.choice("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    else:
        return random.choice(string.ascii_lowercase)

def is_vowel(letter):
    vowels = 'aеёиоуыэюя'
    return letter in vowels

def alphabet_position(letter, cyrillic=False):
    if cyrillic:
        alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    else:
        alphabet = string.ascii_lowercase
    return alphabet.index(letter.lower()) + 1

def letter_from_position(position, cyrillic=False):
    if cyrillic:
        alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    else:
        alphabet = string.ascii_lowercase
    return alphabet[position - 1]

def encrypt(text, matrix_size=None, cyrillic=False):
    # Remove non-alphanumeric characters from the text
    text = ''.join(filter(str.isalnum, text))

    # Calculate the matrix size if not provided
    if not matrix_size:
        matrix_size = int(len(text) ** 0.5)
        if matrix_size ** 2 < len(text):
            matrix_size += 1

    # Create an empty matrix
    encrypted_matrix = [['' for _ in range(matrix_size)] for _ in range(matrix_size)]

    # Create a list of available positions in the matrix and shuffle them randomly
    available_positions = [(x, y) for x in range(matrix_size) for y in range(matrix_size)]
    random.shuffle(available_positions)

    print("Text to encrypt:", text)
    print("Matrix size:", matrix_size)

    # Iterate through each letter in the text
    for letter in text:
        # Pop a random position from the list of available positions
        x, y = available_positions.pop()

        # Generate a random letter different from the current letter
        random_letter = generate_random_letter(cyrillic)
        while random_letter == letter:
            random_letter = generate_random_letter(cyrillic)

        # Choose a random position (1, 2, or 3) for the letter within the slot
        position = random.randint(1, 3)

        # Calculate the prefix based on the random letter and position
        print('random_letter:', random_letter)
        if is_vowel(random_letter):
            prefix = letter_from_position(
                alphabet_position(random_letter, cyrillic) - position + 1,
                cyrillic
            )
            print('prefix vowel:', prefix, 'random_letter:',random_letter)
        else:
            prefix = letter_from_position(
                alphabet_position(random_letter, cyrillic) + position - 1,
                cyrillic
            )
            print('prefix consonant:', prefix, 'random_letter:',random_letter)

        x_suffix = letter_from_position(x + 1, cyrillic)
        y_suffix = letter_from_position(y + 1, cyrillic)

        encrypted_matrix[x][y] = prefix + x_suffix + letter + random_letter + y_suffix

    # Fill the remaining positions in the matrix with random letters
    for x, y in available_positions:
        encrypted_matrix[x][y] = generate_random_letter(cyrillic) * 5

    return encrypted_matrix

text = "пример"
encrypted_matrix = encrypt(text, cyrillic=True)
print("\nEncrypted matrix:")
for row in encrypted_matrix:
    print(row)

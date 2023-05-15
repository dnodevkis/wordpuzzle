import re

def word_endings(text):
    text = text.replace("\n", " ").lower()
    words = re.findall(r'\b[а-яёa-z]+[,.:;!?]*', text)

    word_endings_dict = {}
    for i, word in enumerate(words, start=1):
        # Find the trailing symbols
        trailing_symbols = re.findall(r'[,.:;!?]', word)

        # Remove the trailing symbols from the word
        word = re.sub(r'[,.:;!?]', '', word)

        # Get the part of the word that is longer than 6 characters
        long_part = word[6:]

        # Add the trailing symbols to the long_part
        long_part += "".join(trailing_symbols)

        # Store the long_part in the dictionary
        word_endings_dict[i] = long_part

    return word_endings_dict

multiline_text = '''Все думали что, в зоне?! риска только художники.'''
word_endings_dict = word_endings(multiline_text)
print(word_endings_dict)

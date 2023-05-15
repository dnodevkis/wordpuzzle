import re

def transform_text(text):
    # Remove newlines and convert the text to lowercase
    text = text.replace("\n", " ").lower()

    # Use a regular expression to find words consisting of English or Russian alphabet characters
    words = re.findall(r'\b[а-яёa-z]+\b', text)

    return words

# Example multiline text
multiline_text = '''Все думали что в зоне риска только художники, но нейросети пришли за музыкантами.
Местами вообще не отличить это реально кавер или генерация. Особенно круто что у всяких дрейков и кендриков ламаров сохраняется акцент.'''

transformed_words = transform_text(multiline_text)

print(transformed_words)

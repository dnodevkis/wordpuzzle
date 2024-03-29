# Словарь с отображением букв на химические элементы и индексы
char_to_chem = {
    'а': 'S',  # Сера
    'б': 'He',  # Гелий
    'в': 'Li',  # Литий
    'г': 'Be',  # Бериллий
    'д': 'B',   # Бор
    'е': 'C',   # Углерод
    'ё': 'N',   # Азот
    'ж': 'O',   # Кислород
    'з': 'F',   # Фтор
    'и': 'Ne',  # Неон
    'й': 'Na',  # Натрий
    'к': 'Mg',  # Магний
    'л': 'Al',  # Алюминий
    'м': 'Si',  # Кремний
    'н': 'P',   # Фосфор
    'о': '₂',   # Индекс два
    'п': 'Cl',  # Хлор
    'р': 'Ar',  # Аргон
    'с': 'K',   # Калий
    'т': '₃',  # Индекс три
    'у': 'Sc',  # Скандий
    'ф': 'Ti',  # Титан
    'х': 'V',   # Ванадий
    'ц': 'Cr',  # Хром
    'ч': 'Mn',  # Марганец
    'ш': 'Fe',  # Железо
    'щ': 'Co',  # Кобальт
    'ъ': 'Ni',  # Никель
    'ы': 'Cu',  # Медь
    'ь': 'Zn',  # Цинк
    'э': 'Ga',  # Галлий
    'ю': 'Ge',  # Германий
    'я': 'As',  # Мышьяк
    '.': '₄',   # Символ стрелочки перехода
    ' ': ' → ',   # Индекс 4
    ',': '↑',   # Символ стрелочки перехода
    
}

def subscript(num):
    """Функция для преобразования обычных цифр в нижний индекс."""
    subscript_mapping = {
        '0': '₀', '1': '₁', '2': '₂', '3': '₃',
        '4': '₄', '5': '₅', '6': '₆', '7': '₇',
        '8': '₈', '9': '₉'
    }
    return ''.join(subscript_mapping[digit] for digit in str(num))

def encrypt_text(text):
    encrypted_text = ''
    for char in text.lower():  # Преобразование текста в нижний регистр для удобства
        if char in char_to_chem:
            encrypted_text += char_to_chem[char]
        else:
            encrypted_text += char  # Если символ не найден в словаре, оставить его без изменений
    
    # Временная замена пробелов на уникальный символ
    encrypted_text = encrypted_text.replace('.', '\u200B')  # Замена пробелов на символ нулевой ширины
    # Теперь можно безопасно заменить запятые на пробелы и временный символ обратно на запятые
    encrypted_text = encrypted_text.replace(',', '.')
    encrypted_text = encrypted_text.replace('\u200B', ',')
    
    return encrypted_text

# Тестирование функции
text = "Лол, смотри как придумал для паладинов"
encrypted_text = encrypt_text(text)
print(encrypted_text)  # Вывод: "CAlGaSSi,,k,k,dAl?" (предполагая, что словарь был дополнен для всех букв)

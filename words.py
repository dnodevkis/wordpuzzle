import random

lines = ['заключенный',
'некогда',
'союз',
'вновь',
'становится',
'актуален',
'очень',
'скоро',
'на',
'мир',
'людей',
'обрушится',
'вся',
'мощь',
'и',
'злоба',
'тартара',
'в',
'замке',
'кирсол',
'откроется',
'портал',
'и',
'армии',
'демонов',
'хлынут',
'на',
'земли',
'лангиниона',
'мы',
'вновь',
'обретём',
'территории',
'и',
'величие',
'которые',
'некогда',
'утратили',
'У',
'нас',
'есть',
'союзники',
'среди',
'них',
'встречаются',
'даже',
'люди.',
'как',
'бы',
'странно',
'это',
'не',
'звучало,',
'но',
'именно',
'люди',
'помогут',
'хранителю',
'врат',
'открыть',
'портал',
'и',
'этим',
'докажут',
'свою',
'верность',
'общему',
'делу.',
'за',
'человеком',
'присматривает',
'сам',
'страж,',
'правда',
'до',
'поры',
'он',
'находится',
'в',
'человеческом',
'обличии',
'союзник',
'передал',
'нам',
'список',
'необходимого',
'для',
'открытия',
'врат',
'в',
'мир',
'тьмы',
'ваша',
'задача',
'проста',
'нужно',
'как',
'можно',
'быстрей',
'собрать',
'всё',
'из',
'представленного',
'списка',
'и',
'передать',
'предметы',
'человеку',
'в',
'чьих',
'руках',
'сосредоточена',
'магия',
'он',
'будет',
'ждать',
'действовать',
'нужно',
'осторожно',
'и',
'быстро',
'человек',
'оградит',
'замок',
'от',
'внешних',
'посягательств',
'никто',
'из',
'ушедших',
'воинов',
'империи',
'не',
'сможет',
'нанести',
'удар',
'со',
'спины',
'замок',
'падёт',
'быстро',
'а',
'помимо',
'замка',
'мы',
'получим',
'еще',
'один',
'козырь',
'в',
'виде',
'императорского',
'военачальника',
'его',
'можно',
'дорого',
'продать',
'или',
'убить,',
'лишив',
'имперскую',
'змею',
'одной',
'из',
'голов',
'собрать',
'вам',
'надлежит',
'следующее',
'ритуальные',
'свечи',
'первородную',
'тьму',
'кристаллы',
'света',
'и',
'тьмы',
'нутро',
'некромантического',
'паука',
'сам',
'носитель',
'дара',
'также',
'ищет',
'компоненты',
'но',
'своими',
'способами',
'во',
'избежание',
'провала',
'операции',
'следует',
'собрать',
'всё',
'самостоятельно',
'если',
'человек',
'решит',
'нас',
'предать,',
'мы',
'найдем',
'способ',
'открыть',
'врата',
'и',
'без',
'его',
'участия',
'действуйте',
'незамедлительно']
vowels = [ 'а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я', 'ь', 'ъ']
consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
word_ends_dict = {}




for i in range(len(lines)):    
    word_lenght = len(lines[i])
    word = lines[i]
    word_vowels = []
    word_vowels_pos = []
    word_consonants = []
    word_consonants_pos = []
    even_word_flag = i % 2

    # Превращаем слово в шестибуквенное
    if len(word) > 6:
        word_6 = word[:6]
        # Нужно собрать окончания в отдельный словарь TBD
        word_ending = word[6:]
        word_ends_dict[i+1] = word_ending
    elif len(word) < 6:
        new_letters = 6 - word_lenght
        word_6 = []
        for i in range(word_lenght):
            word_6.append(word[i])
        for i in range(new_letters):
            word_6.append(alphabet[random.randrange(0, 33)])
    elif len(word) == 6:
        word_6 = word


    for i in range(len(word_6)): 
        # Составляем массив гласных
        if word_6[i] in vowels:
            word_vowels.append(word_6[i])
            word_vowels_pos.append(i)

        # Составляем массив согласных
        elif word_6[i] in consonants:
            word_consonants.append(word_6[i])
            word_consonants_pos.append(i)
    word_vowels_new = word_vowels[-1:] + word_vowels[:-1]
    word_consonants_new = word_consonants[-1:] + word_consonants[:-1]

    # Собираем слово обратно (смещение гласных) для нечетных слов
    if even_word_flag == 0:
        new_word_array = []
        for i in range(len(word_6)):
            if i in word_vowels_pos:
                new_word_array.append(word_vowels_new[0])
                word_vowels_new.remove(word_vowels_new[0])

            if i in word_consonants_pos:
                new_word_array.append(word_consonants[0])
                word_consonants.remove(word_consonants[0])

    # Собираем слово обратно (смещение согласных) для четных слов
    if even_word_flag == 1:
        new_word_array = []
        for i in range(len(word_6)):
            if i in word_vowels_pos:
                new_word_array.append(word_vowels[0])
                word_vowels.remove(word_vowels[0])

            if i in word_consonants_pos:
                new_word_array.append(word_consonants_new[0])
                word_consonants_new.remove(word_consonants_new[0])

    # Считаем количество букв в слове и добавляем буквы
    random_letter_pos = (random.randrange(0, 7))
    new_word_array.insert(random_letter_pos, alphabet[word_lenght-1])
    new_word_array.insert(0, alphabet[random_letter_pos+1])
    new_word = ''.join(new_word_array)
    print(new_word)
print(word_ends_dict)



# Вторая задача:

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков
#
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо
# только английские, либо только русские буквы.
#
# Пример:
# ноутбук => 12


flag = True

while flag:
    my_word = input('Введите слово на английском или русском: ')
    if my_word.isalpha():
        my_word = str(my_word).upper()
        flag = False
    else:
        print('Введите корректное слово на английском или русском')

rus = False
kirillic = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

for i in kirillic:
    if i in my_word.lower():
        rus = True

scrabble_dict_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ',
                 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
scrabble_dict_eng = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP',
                 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}

points_summ = 0

if rus is True:
    for i in my_word:
        for key, value in scrabble_dict_ru.items():
            if i in value:
                points_summ = points_summ + key
else:
    for i in my_word:
        for key, value in scrabble_dict_eng.items():
            if i in value:
                points_summ = points_summ + key

print(points_summ)
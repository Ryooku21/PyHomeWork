# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


flag = True

while flag:
    first_set_length = input('Введите длину первого множества: ')
    if first_set_length.isdigit():
        first_set_length = int(first_set_length)
        flag = False
    else:
        print('Введите корректное положительное число')

flag = True

while flag:
    second_set_length = input('Введите длину второго множества: ')
    if second_set_length.isdigit():
        second_set_length = int(second_set_length)
        flag = False
    else:
        print('Введите корректное положительное число')

first_set = [None]*first_set_length
second_set = [None]*second_set_length
set_result = []

for i in range(len(first_set)):
    first_set[i] = int(input('Введите элементы первого множества: '))

for j in range(len(second_set)):
    second_set[j] = int(input('Введите элементы второго множества: '))

print('Первое множество чисел:')
print(first_set)
print('Второе множество чисел:')
print(second_set)

for k in range(first_set_length + second_set_length):
    if (k in first_set) and (k in second_set):
        set_result += [k]

if len(set_result) > 0:
    print(f'Одинаковыми числами в обоих заданных множествах являются: {set_result}')
else:
    print('В заданных множествах нет одинаковых чисел.')
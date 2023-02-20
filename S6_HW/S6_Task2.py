# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


from random import randint

flag = True

while flag:
    minimum = input('Введите минимальное значения диапазона: ')
    if minimum.isdigit():
        minimum = int(minimum)
        flag = False
    else:
        print('Введите корректное положительное число.')

flag = True

while flag:
    maximum = input('Введите максимальное значения диапазона: ')
    if maximum.isdigit():
        maximum = int(maximum)
        flag = False
    else:
        print('Введите корректное положительное число.')

my_list = []
my_list_indexes = []

for i in range(10):
    my_list.append(randint(0, 10))

print(my_list)

for i in range(len(my_list)):
    if my_list[i] >= minimum and my_list[i] <= maximum:
        my_list_indexes.append(i)

print(f'Индексы элементов списка, которые попадают в заданный диапазон: {my_list_indexes}')
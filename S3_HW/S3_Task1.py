# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению.


from random import randint

flag = True

while flag:
    my_list_length = input('Введите длину списка: ')
    if my_list_length.isdigit():
        my_list_length = int(my_list_length)
        flag = False
    else:
        print('Введите корректное положительное число')

flag = True

while flag:
    number_to_find = input('Введите число от 1 до 100 которое необходимо найти: ')
    if number_to_find.isdigit():
        number_to_find = int(number_to_find)
        flag = False
    else:
        print('Введите корректное число от 1 до 100')

my_list = []
count_number_to_find = 0
numbers_diff = 100

for i in range(my_list_length):
    my_list.append(randint(1, 100))

print(my_list)

for j in range(len(my_list)):
    if my_list[j] == number_to_find:
        count_number_to_find += 1

if count_number_to_find > 0:
    print(f'Указанное число встречается в заданном списке {count_number_to_find} раз')
else:
    for k in range(len(my_list)):
        if abs(my_list[k] - number_to_find) < numbers_diff:
            numbers_diff = abs(my_list[k] - number_to_find)
            count_number_to_find = my_list[k]
    print(f'Искомое число не найдено, максимально близкое ему по значению {count_number_to_find}')








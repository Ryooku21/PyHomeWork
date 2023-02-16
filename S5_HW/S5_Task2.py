# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


flag = True

while flag:
    my_number_one = input('Введите первое число: ')
    if my_number_one.isdigit():
        my_number_one = int(my_number_one)
        flag = False
    else:
        print('Введите корректное положительное число.')

flag = True

while flag:
    my_number_two = input('Введите второе число: ')
    if my_number_two.isdigit():
        my_number_two = int(my_number_two)
        flag = False
    else:
        print('Введите корректное положительное число.')


def summ_numbers(num_a, num_b):
    if num_a == 1:
        return num_b + 1
    elif num_b == 1:
        return num_a + 1
    else:
        return summ_numbers(num_a + 1, num_b - 1)


print(f'Сумма введенных чисел {my_number_one} и {my_number_two} равна: {summ_numbers(my_number_one, my_number_two)}')
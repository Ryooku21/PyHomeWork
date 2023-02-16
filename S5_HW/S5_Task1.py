# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.


flag = True

while flag:
    my_number = input('Введите натуральное число: ')
    if my_number.isdigit():
        my_number = int(my_number)
        flag = False
    else:
        print('Введите корректное положительное число.')

flag = True

while flag:
    my_num_degree = input('Введите степень, в которую необходимо возвести число: ')
    if my_num_degree.isdigit():
        my_num_degree = int(my_num_degree)
        flag = False
    else:
        print('Введите корректное положительное число.')


def recursion_degree(num, degree):
    if degree == 1:
        return num
    else:
        return num * recursion_degree(num, degree - 1)


print(f'Число {my_number} в степени {my_num_degree} равно: {recursion_degree(my_number, my_num_degree)}')
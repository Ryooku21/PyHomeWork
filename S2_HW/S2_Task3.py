# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8


while True:
    stop_number = input('Введите натуральное число: ')
    if stop_number.isdigit():
        stop_number = int(stop_number)
        break
    else:
        print('Введите корректное натуральное число')

grade_number = 0

print()
print(f'Все целые степени числа 2, не превосходящие {stop_number}:')

for i in range(stop_number):
    if grade_number < stop_number:
        grade_number = 2 ** i
        if grade_number < stop_number:
            print(grade_number, end=" ")
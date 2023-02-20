# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


flag = True

while flag:
    first_element = input('Введите первый элемент арифметической прогресии: ')
    if first_element.isdigit():
        first_element = int(first_element)
        flag = False
    else:
        print('Введите корректное положительное число.')

flag = True

while flag:
    difference = input('Введите разность: ')
    if difference.isdigit():
        difference = int(difference)
        flag = False
    else:
        print('Введите корректное положительное число.')

flag = True

while flag:
    elements_total = input('Введите количество элементов: ')
    if elements_total.isdigit():
        elements_total = int(elements_total)
        flag = False
    else:
        print('Введите корректное положительное число.')

result = []
for i in range(elements_total):
    result.append(first_element + i * difference)

print('Список, заполненный элементами арифметической прогресии:')
print(result)
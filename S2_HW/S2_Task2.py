# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2


while True:
    summ = input('Введите сумму чисел: ')
    if summ.isdigit():
        summ = int(summ)
        break
    else:
        print('Введите корректное натуральное число')

while True:
    multiply = input('Введите произведение чисел: ')
    if multiply.isdigit():
        multiply = int(multiply)
        break
    else:
        print('Введите корректное натуральное число')

discriminant = 0
first_number = 0
second_number = 0

if summ % 2 != 0:                              # Ищем дискриминант для уравнения x2 - (summ)y + multiply = 0
    discriminant = summ ** 2 - (multiply * 4)
else:
    discriminant = (summ / 2) ** 2 - multiply

if (summ <= 3) and (multiply <= 3):                 # Проверяем если введенные числа меньше 4
    print('Задача не имеет решения')
    exit(0)
elif (discriminant > 0) or (summ % 2 == 0):        # Уравнение для нечетного второго коэффициента
    first_number = (summ / 2) + discriminant ** 0.5
    second_number = (summ / 2) - discriminant ** 0.5
elif (discriminant > 0) and (summ % 2 != 0):       # Уравнение для четного второго коэффициента
    first_number = (summ + discriminant ** 0.5) / 2
    second_number = (summ - discriminant ** 0.5) / 2
elif discriminant == 0:                        # Уравнение для дискриминанта равного 0
    first_number = summ / 2
    second_number = summ / 2
elif discriminant < 0:                         # Если дискриминант меньше 0, то уравнение не имеет корней
    print('Задача не имеет решения')
    exit(0)

# Т.к. из-за вычислений в формулах получается значение float, то целые числа выводятся с 0 после запятой.
# Чтобы убрать этот эфект и при этом не испортить решение, вычитаем интовую часть из числа и проверяем есть ли остаток.
if (first_number - int(first_number) != 0) or (second_number - int(second_number) != 0):
    print('Задача не имеет решения')
else:
    print(f'Петя задумал числа {int(first_number)} и {int(second_number)}')









# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# Пример:
# 4 -> 1 2 3 4
# 9


from random import randint

flag = True

while flag:
    cultivation_count = input('Введите количество грядок: ')
    if cultivation_count.isdigit():
        cultivation_count = int(cultivation_count)
        flag = False
    else:
        print('Введите корректное число')

cultivation = []

for i in range(cultivation_count):
    cultivation.append(randint(0, 10))

print(f'На каждой грядке созрело следующее количество ягод: {cultivation}')

max_berries = 0

for j in range(len(cultivation) - 1):
    if j == 0:
        if cultivation[len(cultivation) - 1] + cultivation[j] + cultivation[j + 1] > max_berries:
            max_berries = cultivation[len(cultivation) - 1] + cultivation[j] + cultivation[j + 1]
    elif j == len(cultivation) - 1:
        if cultivation[0] + cultivation[j] + cultivation[j - 1] > max_berries:
            max_berries = cultivation[0] + cultivation[j] + cultivation[j - 1]
    elif cultivation[j-1] + cultivation[j] + cultivation[j + 1] > max_berries:
        max_berries = cultivation[j-1] + cultivation[j] + cultivation[j + 1]

print(f'Максимальное количество ягод, которое может собрать модуль: {max_berries}')
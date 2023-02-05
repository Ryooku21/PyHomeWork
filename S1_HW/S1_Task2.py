# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10


cranes_total = int(input('Введите количество журавликов: '))
kate = cranes_total / 3 * 2
the_boys = int()

if (cranes_total - kate) % 2 != 0 or cranes_total == 0 or cranes_total < 0:
    print('Решение задачи невозможно')
else:
    the_boys = kate / 4
    print(f'Катя собрала {int(kate)} журавликов, Петя и Сережа по {int(the_boys)}')

# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no


lucky_ticket = int(input('Введите номер билета: '))
if lucky_ticket > 999999 or lucky_ticket < 100000:
    print('Номер билета должен состоять из 6 цифр')
    exit()

lucky_part_one = lucky_ticket // 1000
lucky_part_two = lucky_ticket % 1000
lucky_part_one = (lucky_part_one // 100) + (lucky_part_one // 10 % 10) + (lucky_part_one % 10)
lucky_part_two = (lucky_part_two // 100) + (lucky_part_two // 10 % 10) + (lucky_part_two % 10)

if lucky_part_one != lucky_part_two:
    print('Несчастный билет')
else:
    print('Счастливый билет!')


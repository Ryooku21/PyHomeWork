# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# *Пример:
# 5 -> 1 0 1 1 0


from random import randint

heads = 0
tails = 0

while True:
    coin_count = input('Введите количество монет: ')
    if coin_count.isdigit():
        coin_count = int(coin_count)
        break
    else:
        print('Введите корректное число')

for i in range(coin_count+1):
    coin_side = randint(0, 1)
    if coin_side == 0:
        heads += 1
    elif coin_side == 1:
        tails += 1

if heads > tails:
    print(f'Минимальное количество монет, которое необходимо перевернуть {tails}')
else:
    print(f'Минимальное количество монет, которое необходимо перевернуть {heads}')



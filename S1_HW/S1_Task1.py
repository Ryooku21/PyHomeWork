# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


number = int(input("Введите трехзначное число:"))
result = int()
if number < 100 or number > 999:
    print('Число должно быть трехзначным!')
else:
    result = (number // 100) + (number // 10 % 10) + (number % 10)
print(f'Сумма цифр в чиселе = {result}')

number = int(input('enter number'))
f1 = 0
f2 = 1
i = 2
while i <= number:
    f_summ = f1 + f2
    f1 = f2
    f2 = f_summ
    i += 1
    if f_summ == number:
        print(i)
        break
    elif f_summ > number:
        print(-1)
        break






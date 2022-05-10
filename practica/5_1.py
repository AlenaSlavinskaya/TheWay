# Задача 1 (2 способ)
a = input('Введите семизначное число: ')
d = 0 # Счетчик четных цифр
f = 0 # Счетчик нечетных цифр
c = []
for i in a:
    i = int(i)
    c.append(i)
    if i % 2 == 0:
        d += 1
    else:
        f += 1
if d > f:
    print(sum(c))
else:
    print(c[0] * c[2] * c[5])
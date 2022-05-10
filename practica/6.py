# Задача 2
# Посчитать, сколько раз встречается определенная цифра(цифра – это от 0 до 9) в списке чисел.
# Количество введенных чисел в список и искомая цифра задаются с клавиатуры. Числа выбираются рандомно.

import random

a = input("Введите количество чисел в списке: ")
b = input("Введите искомую цифру: ")
abc = []
st = 0

for i in range(int(a)):
    abc.append(random.randint(0,100))
print(abc)
for el in abc:
    el = str(el)
    h = el.count(b)
    if h > 0:
        st += h
    else:
        continue
print(st)
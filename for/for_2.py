# Задача 1. Вводится трехзначное число. Находим сумму цифр числа

a = 0
b = input("Введите трехзначное число: ")
for i in b:
    i = int(i)
    a = a + i
print("Сумма цифр числа: ",a)
#Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать

a = [1,2,3,4,2,6,4,6,7,89,6,6]
b = 0
c = 0
for i in a:
    if a.count(i) >= 2:
        b +=1
        c = b//2
print(c)
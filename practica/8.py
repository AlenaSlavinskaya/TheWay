# Задача 4
# Дан список.
# Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

a = ['mushroom',3,'melon','lemon',254,'seafood',876557889,'prunes','lemon',12,'melon',254,'pomegranate','peach',876557889]
b = []

for i in a:
    if a.count(i) == 1:
        b.append(i)
    else:
        continue
else:
    print(b)
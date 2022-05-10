# Задача №1
# Значениями словаря могут быть и списки.
# Создайте словарь с ключами BMW, Tesla и списками из 3х моделей в качестве значений.
# Выведите первое и последнее значения каждого из ключей.

avto = {'BMW': ['X5 M Competition', 'M850i xDrive Cabrio', 'M8 Gran Coupe'],
       'Tesla': ['Model Y', 'Roadster', 'Model X']}

for key, value in avto.items():
    print(value[0],',',value[-1])
# a = {}
# print(type(a))
# a = {'
# 1': 123, 2:'hello'}

# a['3'] = [1,2,3,4,5]
# a[3] = (2,3,4,5,6,7)
# print(a['3'][0])

# d = dict(short='dict', long ='dictionary')
# d_2 = dict([(1,1),(2,'tree')])

#
# d = dict.fromkeys(['a','b']) # словари с пустыми значениями, никакого типа данных в себе не имеют
# d_2 = dict.fromkeys(['a','b'],100) # значение 100, которое будет у всех ключей. Если нужно создать словарь с уникальными ключами, но с одинаковыми значениями
#
# print(d_2)
# d={a: a**2 for a in range(7)} # Генерация словаря
# print(d)
a = [1,2,3,4,5]
b = ['hello','world','sun','daddy','mummy']
d = dict(zip(a,b))
# print(d)




if 2 in d:
    print(2)

print(d)
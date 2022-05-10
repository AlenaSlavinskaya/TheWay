# Есть словарь песен группы Depeche Mode violator
# Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых больше 5 минут
# Создайте новый словарь тех песен, название которых  состоит из одного слова

songsdict = {
'World in My Eyes': 4.76,
'Sweetest Perfection': 5.43,
'Personal Jesus': 4.56,
'Halo': 4.30,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.6,
'Policy of Truth': 4.88,
'Blue Dress': 4.18,
'Clean': 5.68,
}

print("Общее время звучания песен:",sum(songsdict.values()))
a = []

for k, v in songsdict.items():
    c = float(v)
    if c > 5.00:
        a += {k}
    else:
        continue
print("Cписок песен, время звучаниях которых больше 5 минут:", a)

songsdict_2 = {}

for k, v in songsdict.items():
    if k.isalpha() == True:
        songsdict_2.update([(k,v)])
    else:
        continue
print(songsdict_2)
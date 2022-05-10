# Отсортировать список и оставить в нем только уникальные элементы

sp_1 = ['peper',3,'salt','fennel',254,'peper',876557889,'salt','buter',254,'tomato','12',876557889]
sp_2 = []

for a in sp_1:
    if sp_1.count(a) > 1:
        continue
    else:
        sp_2.append(a)
else:
    print(sp_2)

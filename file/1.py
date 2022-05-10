# f = open('text.txt','r')
# print(f.readlines()) # Читает весь файл, readline() читает первую строку файла

# for i in f: # тоже для чтения файла
#     print(i)

# print(*f) # распечатывает всё, что содержится в текстовом файле, но так тяжелее пользоваться
# f.close()

# f = open('text.txt','w') #  запись, старый файл стирается

# f = open('text.txt','a') # дозапись файла
# f.write('sunday\nsaturday')

# f = open('text.txt','w') # запись в файл
# l =['hello','red','blue']
#
# for i in l:
#     f.write(i+'\n')

# with open('text_1.txt','w') as f: # работа с текстом о одном блоке, закрывать не нужно
#     f.write('Hey')

with open('text_1.txt', 'r') as f:
    print(f.readlines())
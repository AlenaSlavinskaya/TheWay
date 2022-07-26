# Создайте метод класса для работы с БД
# В БД
# 1. Если передан 1 аргумент, вставить в таблицу запись с числом 3
# 2. Если переданы 2 аргумента: проверить или второй аргумент является числом.
# 3. Если условие верно, то удалить первую запись с БД
# 4. Если переданы 2 аргумента, их значения не известны, а 3 является числом, то обновить на число 77 запись 3.

import sqlite3
import random

conn = sqlite3.connect('z_3.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER) ''')
r = random.randint(1,20)
cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (?)''',(r,))
conn.commit()
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k)
class A:
    def baz(self, a =None,b=None,c=None):
        if a is not None and b is None and c is None:
            cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (3)''')
            conn.commit()
        elif a is not None and b is not None and c is None:
            if type(b) is int:
                cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
                conn.commit()
        elif a is not None and b is not None and type(c) is int :
            cursor.execute('''UPDATE tab_1 SET col_1 = 77 WHERE id = 3''')


example = A()
example.baz(3,'hello',9)
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k)
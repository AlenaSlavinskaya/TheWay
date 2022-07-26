# 1.Сформулируйте SQL запрос для создания таблицы book.
# 2.Занесите новую строку в таблицу book.
# 3.Выбрать информацию о всех книгах из таблицы book.

import sqlite3

conn = sqlite3.connect("book.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS book(book_id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(50),author VARCHAR(30), price DECIMAL(8, 2), amount INT)''')
cursor.execute('''INSERT INTO book(title,author,price,amount) VALUES ('Blackberry winter','Sarah Jio',16.83,23)''')
conn.commit()
cursor.execute('''SELECT*FROM book''')
p = cursor.fetchall()
print(p)
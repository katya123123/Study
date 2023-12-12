import sqlite3

con1 = sqlite3.connect("book24_genre_desc.db")
#con2= sqlite3.connect()
cur1 = con1.cursor("select Жанр_первый, Жанр_второй from Books")
#cur2 = con2.cursor("select жанр from livelib.db")
results = cur1.fetchall()
print(results)
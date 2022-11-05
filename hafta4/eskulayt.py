import sqlite3

bag = sqlite3.connect("a.vt") # Tabloya bağlanıyoruz

cursor = bag.cursor() # vt üzerinde işlem yapmak için cursor kullanıyoruz

cursor.execute("""CREATE TABLE IF NOT EXISTS `pariteler`(
	            id INTEGER PRIMARY KEY AUTOINCREMENT,
	            otime DATETIME,
	            open FLOAT,
	            high FLOAT,
	            low FLOAT,
	            close FLOAT);""")



bag.close() # işimiz bitince kapatıyoruz

# import sqlite3 as sq

# db = sq.connect('database/pyty.db', check_same_thread=False)
# cur = db.cursor()
# def db_table_val(user_id: int, user_name: str):
# 	cur.execute('INSERT INTO user (user_id, user_name) VALUES (?, ?)', (user_id, user_name))
# 	db.commit()

import sqlite3


async def starting_id_name(user: int, name: str):
	db = sqlite3.connect('m0kas1.db')
	c = db.cursor()

	c.execute('''CREATE TABLE IF NOT EXISTS tik (
        user_id INTEGER UNIQUE,
        username TEXT,
        factory TEXT,
        fio TEXT,
        podrasd TEXT,
        oblst TEXT,
        nasv_prdl TEXT,
        opis_probl TEXT,
        photo_probl TEXT,
        resh_probl TEXT,
        photo_resh TEXT
    )''')

	# user = int(input())
	# name = input()

	c.execute(f"SELECT * FROM tik WHERE user_id = {user}")
	all = c.fetchone()
	# print(all)
	if all:
		print("Такой пользователь уже есть!")
	else:
		c.execute("INSERT INTO tik (user_id, username, factory) VALUES (?, ?, ?)", (user, f"{name}", 0))
		db.commit()
		c.execute(f"SELECT * FROM tik WHERE user_id = {user}")
		k = c.fetchone()
		print(k)
	db.commit()
	db.close()


async def factory_tip(factory_job: str, user: int):
	db = sqlite3.connect('m0kas1.db')
	c = db.cursor()
	c.execute(f"UPDATE tik SET factory = '{factory_job}' WHERE user_id = {user}")
	db.commit()
	db.close()

async def podresdel(pod: str, user: int):
	db = sqlite3.connect('m0kas1.db')
	c = db.cursor()
	c.execute(f"UPDATE tik SET podrasd = '{pod}' WHERE user_id = {user}")
	db.commit()
	db.close()


async def fio_cross(fio_text: str, user: int):
	db = sqlite3.connect('m0kas1.db')
	c = db.cursor()
	c.execute(f"UPDATE tik SET fio = '{fio_text}' WHERE user_id = {user}")
	db.commit()
	db.close()

async def oblast_tip(oblst_uluch: str, user: int):
	db = sqlite3.connect('m0kas1.db')
	c = db.cursor()
	c.execute(f"UPDATE tik SET oblst = '{oblst_uluch}' WHERE user_id = {user}")
	db.commit()
	db.close()

async def nasvani(nasv: str, user: int):
	db = sqlite3.connect('m0kas1.db')
	c = db.cursor()
	c.execute(f"UPDATE tik SET nasv_prdl = '{nasv}' WHERE user_id = {user}")
	db.commit()
	db.close()


async def opicka(picka: str, user: int):
	db = sqlite3.connect('m0kas1.db')
	c = db.cursor()
	c.execute(f"UPDATE tik SET opis_probl = '{picka}' WHERE user_id = {user}")
	db.commit()
	db.close()

async def photochka(photka: str, user: int):
	db = sqlite3.connect('m0kas1.db')
	c = db.cursor()
	c.execute(f"UPDATE tik SET photo_probl = '{photka}' WHERE user_id = {user}")
	db.commit()
	db.close()

async def reshka(resh: str, user: int):
	db = sqlite3.connect('m0kas1.db')
	c = db.cursor()
	c.execute(f"UPDATE tik SET resh_probl = '{resh}' WHERE user_id = {user}")
	db.commit()
	db.close()

async def photochka_resh(reshil: str, user: int):
	db = sqlite3.connect('m0kas1.db')
	c = db.cursor()
	c.execute(f"UPDATE tik SET photo_resh = '{reshil}' WHERE user_id = {user}")
	db.commit()
	db.close()

async def return_basa(user: int):
	db = sqlite3.connect('m0kas1.db')
	c = db.cursor()
	c.execute(f"SELECT * FROM tik WHERE user_id = {user}")
	l = c.fetchone()
	# print(k)
	db.close()
	return l

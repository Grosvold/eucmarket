import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('adverts.db')
    cur = base.cursor()
    if base:
        print('DataBase connected OK')
    base.execute("CREATE TABLE IF NOT EXISTS adverts(advert_id TEXT PRIMARY KEY, chat_id TEXT, advert_type TEXT, city TEXT, forwarding TEXT, img_0 TEXT, img_1 TEXT, img_2 TEXT, img_3 TEXT, img_4 TEXT, img_5 TEXT, img_6 TEXT, img_7 TEXT, img_8 TEXT, img_9 TEXT, description TEXT, price TEXT, create_time TEXT)")
    base.commit()

def sql_add_command(data):
    cur.execute('INSERT INTO adverts VALUES (:advert_id, :chat_id, :advert_type, :city, :forwarding, :img_0, :img_1, :img_2, :img_3, :img_4, :img_5, :img_6, :img_7, :img_8, :img_9, :description, :price, :create_time)', data)
#    cur.execute('INSERT INTO adverts VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(data))
    base.commit()
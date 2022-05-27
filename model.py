import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def getMenu(jenis):
    try:
        get = cursor.execute("SELECT * FROM data_barang WHERE Jenis=?", (jenis,))
        fetch = get.fetchall()
        return fetch

    except sqlite3.Error as e:
        print(e)

def updateMenu(namaAwal, namaGanti):
    try:
        cursor.execute("UPDATE data_barang SET Nama=? WHERE Nama=?", (namaGanti, namaAwal))
        connection.commit()

    except sqlite3.Error as e:
        print(e)

import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def createDatabase():
    sqlite_create_table_query = '''CREATE TABLE data_barang (
                                Jenis TEXT,
                                Nama TEXT,
                                Keterangan TEXT,
                                Kode INTEGER);'''

    print("Berhasil Terhubung Ke SQLite")
    cursor.execute(sqlite_create_table_query)
    cursor.commit()
    print("SQLite table created")
    cursor.close()

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

def getNama(index):
    try:
        get = cursor.execute("SELECT * FROM data_barang WHERE Kode=?", (index,))
        fetch = get.fetchall()
        return fetch[0][1]

    except sqlite3.Error as e:
        print(e)
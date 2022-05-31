import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def createDatabase():
    """ sebuah fitur untuk membuat tabel database yang didalamnya ada nama dan harga barang """
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
    """ sebuah fitur untuk mengambil data dari database berdasarkan jenis barang """
    try:
        get = cursor.execute("SELECT * FROM data_barang WHERE Jenis=?", (jenis,))
        fetch = get.fetchall()
        return fetch

    except sqlite3.Error as e:
        print(e)

def updateMenu(namaAwal, namaGanti):
    """ sebuah fitur untuk mengganti nama barang dengan parameter nama sekarang dan nama yang akan menjadi ganti """
    try:
        cursor.execute("UPDATE data_barang SET Nama=? WHERE Nama=?", (namaGanti, namaAwal))
        connection.commit()

    except sqlite3.Error as e:
        print(e)

def getNama(index):
    """ sebuah fitur untuk mengambil nama barang berdasarkan kode dari barang """
    try:
        get = cursor.execute("SELECT * FROM data_barang WHERE Kode=?", (index,))
        fetch = get.fetchall()
        return (fetch[0][1]).upper()

    except sqlite3.Error as e:
        print(e)

def getHarga(namaBarang):
    """ sebuah fitur untuk mengambil harga barang berdasarkan nama barang"""
    try:
        get = cursor.execute("SELECT * FROM data_barang WHERE Nama=?", (namaBarang,))
        fetch = get.fetchall()
        return fetch

    except sqlite3.Error as e:
        print(e)

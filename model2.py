from distutils.log import error
import sqlite3

def createDatabase():
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        sqlite_create_table_query = '''CREATE TABLE TB_History (
                                nama_pembeli TEXT,
                                tanggal_pembelian TEXT,
                                jenis_cone TEXT,
                                varian_rasa TEXT,
                                varian_toping TEXT,
                                total_harga TEXT);'''

        print("Berhasil Terhubung Ke SQLite")
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite table created")
        cursor.close()

    except sqlite3.Error as error:
        print("Error Ketika Membuat Table SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")


def count_cone(data):
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Berhasil Terhubung Ke SQLite")

        count = cursor.execute(""" SELECT * FROM TB_History WHERE jenis_cone=?""", (data,))
        rows = count.fetchall()

        return rows

        print("Get data success", rows)
        cursor.close()

    except sqlite3.Error as error:
        print("Gagal Mendapatkan Data Dari Tabel SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            
def count_rasa(data):
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Berhasil Terhubung Ke SQLite")

        count = cursor.execute(""" SELECT * FROM TB_History WHERE varian_rasa=?""", (data,))
        rows = count.fetchall()

        return rows

        print("Get data success", rows)
        cursor.close()

    except sqlite3.Error as error:
        print("Gagal Mendapatkan Data Dari Tabel SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            
def count_toping(data):
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Berhasil Terhubung Ke SQLite")

        count = cursor.execute(""" SELECT * FROM TB_History WHERE varian_toping=?""", (data,))
        rows = count.fetchall()

        return rows

        print("Get data success", rows)
        cursor.close()

    except sqlite3.Error as error:
        print("Gagal Mendapatkan Data Dari Tabel SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            

def getHistory():
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Berhasil Terhubung Ke SQLite")

        count = cursor.execute(""" SELECT * FROM TB_History """)
        rows = count.fetchall()

        return rows

        print("Get data success", rows)
        cursor.close()

    except sqlite3.Error as error:
        print("Gagal Mendapatkan Data Dari Tabel SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def ambilrasa():
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Berhasil Terhubung Ke SQLite")

        count = cursor.execute(""" SELECT DISTINCT varian_rasa FROM TB_History """)
        rows = count.fetchall()

        return rows

        print("Get data success", rows)
        cursor.close()

    except sqlite3.Error as error:
        print("Gagal Mendapatkan Data Dari Tabel SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def ambiltoping():
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Berhasil Terhubung Ke SQLite")

        count = cursor.execute(""" SELECT DISTINCT varian_toping FROM TB_History """)
        rows = count.fetchall()

        return rows

        print("Get data success", rows)
        cursor.close()

    except sqlite3.Error as error:
        print("Gagal Mendapatkan Data Dari Tabel SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def jumlahCone():
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Berhasil Terhubung Ke SQLite")

        count = cursor.execute(""" SELECT jenis_cone FROM TB_History """)
        rows = count.fetchall()

        return rows

        print("Get data success", rows)
        cursor.close()

    except sqlite3.Error as error:
        print("Gagal Mendapatkan Data Dari Tabel SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def insertDatatoDB(*data):
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        count = cursor.execute(""" INSERT INTO TB_History
                              (nama_pembeli, tanggal_pembelian, jenis_cone, varian_rasa, varian_toping, total_harga)
                               VALUES
                              (?,?,?,?,?,?)""",
                              ((data[0]),data[1],data[2],data[3],(data[4]), (data[5])))
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
createDatabase()

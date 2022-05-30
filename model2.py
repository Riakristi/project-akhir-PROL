from distutils.log import error
import sqlite3

from colorama import Cursor

def createDatabase():
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        sqlite_create_table_query = '''CREATE TABLE TB_History (
                                nama_pembeli TEXT NOT NULL,
                                tanggal_pembelian TEXT NOT NULL,
                                ukuran_cup TEXT NOT NULL,
                                varian_rasa TEXT NOT NULL,
                                varian_toping TEXT NOT NULL);'''

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

def viewDataFromDB(jenis,data2):
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Berhasil Terhubung Ke SQLite")

        count = cursor.execute(""" SELECT * FROM TB_History WHERE {}={}""".format(jenis,data2))
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

        count = cursor.execute(""" SELECT varian_rasa FROM TB_History """)
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

def ambiltopping():
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Berhasil Terhubung Ke SQLite")

        count = cursor.execute(""" SELECT varian_toping FROM TB_History """)
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
                              (nama_pembeli, tanggal_pembelian, ukuran_cup, varian_rasa, varian_toping)
                               VALUES
                              (?,?,?,?,?)""",
                              ((data[0]),data[1],data[2],data[3],(data[4])))
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
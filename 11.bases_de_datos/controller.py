from asyncio import streams
from dis import Instruction
import sqlite3 as sql

def create_db():
    conn = sql.connect("streamers.db")
    conn.commit()
    conn.close()

def create_table():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE streamers (
            id int PRIMARY KEY AUTOINCREMENT
            name text,
            followers integer,
            subs integer
        )"""
    )

    conn.commit() # De esta manera aplicamos los cambios
    conn.close()

def insert_row(nombre, followers, subs):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES ('{nombre}', {followers}, {subs})"
    cursor.execute(instruccion)

    conn.commit() # De esta manera aplicamos los cambios
    conn.close()

def read_rows():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall() # Devuelve todos los datos con un formato especifico
    conn.commit()
    conn.close()
    print(datos)

def insert_rows(streamerlist):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES (?,?,?)"
    cursor.executemany(instruccion, streamerlist) # insertas varios de una lista

    conn.commit() # De esta manera aplicamos los cambios
    conn.close()

def read_ordered(field):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall() # Devuelve todos los datos con un formato especifico
    conn.commit()
    conn.close()
    print(datos)

def search(value):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers WHERE name like '{value}%'"
    cursor.execute(instruccion)
    datos = cursor.fetchall() # Devuelve todos los datos con un formato especifico
    conn.commit()
    conn.close()
    print(datos)

def update_fields():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE streamers SET followers=2400000 WHERE name like 'merakio'"
    cursor.execute(instruccion)
    
    conn.commit()
    conn.close()  



def delete_row(value):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    borrar = f"DELETE FROM streamers WHERE subs='{value}'"
    cursor.execute(borrar)
    conn.commit()
    conn.close()
    


if __name__ == "__main__":
    #create_db()
    #create_table()
    #insert_row('Rubius', 1200000, 500000)
    #insert_row('JordiWild', 1000000, 300000)
    #read_rows()
    streamers = [
        ("AuronPlay", 8000000, 20000),
        ("JordiWild", 2500000, 30000),
        ("Merakio", 1200000, 1500)
    ]
    #insert_rows(streamers)
    #read_ordered('followers')
    #search('Jor')
    update_fields()

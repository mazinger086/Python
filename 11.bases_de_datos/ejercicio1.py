import sqlite3 as sql

def crear_db():
    conn = sql.connect("alumnos.db")
    conn.commit()
    conn.close()

def crear_tabla():
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Alumnos(
            id integer PRIMARY KEY AUTOINCREMENT,
            nombre text NOT NULL,
            apellido text NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

def insertar_row(id, nombre, apellido):
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    intruccion = f"INSERT INTO Alumnos VALUES ({id},'{nombre}','{apellido}')"
    cursor.execute(intruccion)
    conn.commit()
    conn.close()


def insertar_rows(lista):
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    intruccion = f"INSERT INTO Alumnos VALUES (?,?,?)"
    cursor.executemany(intruccion, lista)
    conn.commit()
    conn.close()


def busqueda(valor):
    conn = sql.connect("alumnos.db")
    cursor = conn.cursor()
    intruccion = f"SELECT * FROM Alumnos WHERE nombre like '{valor}'"
    cursor.execute(intruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)


if __name__ == "__main__":
    #crear_db()
    #crear_tabla()
    #insertar_row(1,'Gisela', 'Salguero')
    alumnos = [
        (5, 'Romina', 'Sotelo'),
        (6, 'Samantha', 'Ibarra'),
        (7, 'Soledad', 'Isacco'),
        (8, 'Rocio', 'Romaniello')
    ]
    #insertar_rows(alumnos)
    busqueda('soledad')
    
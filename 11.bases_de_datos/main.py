import sqlite3
import getpass


def main():
    username = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")

    if verifica_credenciales():
        print('Login correcto')
    else:
        print('Login incorrecto')

def verifica_credenciales(username, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    print("Query a ejecutar: ", query)
    rows = cursor.execute(query)
    data = rows.fetchone()
    print(data)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()



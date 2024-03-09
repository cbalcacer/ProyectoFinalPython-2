import sqlite3
def conectar():
    conn = sqlite3.connect('escuela.db')
    return conn
def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS estudiante (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS seccion (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS materia (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        duracion_horas INTEGER NOT NULL,
                        aula TEXT NOT NULL,
                        creditos INTEGER NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS maestro (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    crear_tablas()

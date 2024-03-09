import sqlite3

def conectar():
    return sqlite3.connect('escuela.db')

conn = conectar()
cursor = conn.cursor()

# Obtener detalles de la estructura de la tabla 'materia'
cursor.execute("PRAGMA table_info(materia)")
columnas = cursor.fetchall()

for col in columnas:
    print(col)

conn.close()

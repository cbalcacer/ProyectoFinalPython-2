import sqlite3

# Función para conectar a la base de datos
def conectar():
    return sqlite3.connect('escuela.db')

class Estudiante:
    @staticmethod
    def agregar(nombre):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO estudiante (nombre) VALUES (?)", (nombre,))
            conn.commit()
        except sqlite3.Error as e:
            print("Error al agregar estudiante:", e)
        finally:
            conn.close()

    @staticmethod
    def obtener_todos():
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estudiante")
            estudiantes = cursor.fetchall()
            return estudiantes
        except sqlite3.Error as e:
            print("Error al obtener estudiantes:", e)
            return []
        finally:
            conn.close()

    @staticmethod
    def actualizar(id, nombre):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("UPDATE estudiante SET nombre = ? WHERE id = ?", (nombre, id))
            conn.commit()
        except sqlite3.Error as e:
            print("Error al actualizar estudiante:", e)
        finally:
            conn.close()

    @staticmethod
    def eliminar(id):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM estudiante WHERE id = ?", (id,))
            conn.commit()
        except sqlite3.Error as e:
            print("Error al eliminar estudiante:", e)
        finally:
            conn.close()

class Seccion:
    @staticmethod
    def agregar(nombre):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO seccion (nombre) VALUES (?)", (nombre,))
            conn.commit()
        except sqlite3.Error as e:
            print("Error al agregar sección:", e)
        finally:
            conn.close()

    @staticmethod
    def obtener_todos():
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM seccion")
            secciones = cursor.fetchall()
            return secciones
        except sqlite3.Error as e:
            print("Error al obtener secciones:", e)
            return []
        finally:
            conn.close()

    @staticmethod
    def actualizar(id, nombre):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("UPDATE seccion SET nombre = ? WHERE id = ?", (nombre, id))
            conn.commit()
        except sqlite3.Error as e:
            print("Error al actualizar sección:", e)
        finally:
            conn.close()

    @staticmethod
    def eliminar(id):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM seccion WHERE id = ?", (id,))
            conn.commit()
        except sqlite3.Error as e:
            print("Error al eliminar sección:", e)
        finally:
            conn.close()

class Materia:
    @staticmethod
    def agregar(nombre, duracion_horas, aula, creditos):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO materia (nombre, duracion_horas, aula, creditos) VALUES (?, ?, ?, ?)", (nombre, duracion_horas, aula, creditos))
            conn.commit()
        except sqlite3.Error as e:
            print("Error al agregar materia:", e)
        finally:
            conn.close()

    @staticmethod
    def obtener_todos():
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM materia")
            materias = cursor.fetchall()
            return materias
        except sqlite3.Error as e:
            print("Error al obtener materias:", e)
            return []
        finally:
            conn.close()

    @staticmethod
    def actualizar(id, nombre, duracion_horas, aula, creditos):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("UPDATE materia SET nombre = ?, duracion_horas = ?, aula = ?, creditos = ? WHERE id = ?", (nombre, duracion_horas, aula, creditos, id))
            conn.commit()
        except sqlite3.Error as e:
            print("Error al actualizar materia:", e)
        finally:
            conn.close()

    @staticmethod
    def eliminar(id):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM materia WHERE id = ?", (id,))
            conn.commit()
        except sqlite3.Error as e:
            print("Error al eliminar materia:", e)
        finally:
            conn.close()

class Maestro:
    @staticmethod
    def agregar(nombre):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO maestro (nombre) VALUES (?)", (nombre,))
            conn.commit()
        except sqlite3.Error as e:
            print("Error al agregar estudiante:", e)
        finally:
            conn.close()

    @staticmethod
    def obtener_todos():
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM maestro")
            maestros = cursor.fetchall()
            return maestros
        except sqlite3.Error as e:
            print("Error al obtener maestros:", e)
            return []
        finally:
            conn.close()

    @staticmethod
    def actualizar(id, nombre):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("UPDATE maestro SET nombre = ? WHERE id = ?", (nombre, id))
            conn.commit()
        except sqlite3.Error as e:
            print("Error al actualizar maestro:", e)
        finally:
            conn.close()

    @staticmethod
    def eliminar(id):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM maestro WHERE id = ?", (id,))
            conn.commit()
        except sqlite3.Error as e:
            print("Error al eliminar maestros:", e)
        finally:
            conn.close()

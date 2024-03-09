from modelos import Estudiante, Seccion, Materia, Maestro


def menu_principal():
    while True:
        print("\nSISTEMA DE INSCRIPCIÓN ESCOLAR")
        print("1. Estudiantes")
        print("2. Secciones")
        print("3. Materias")
        print("4. Maestros")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_estudiantes()
        elif opcion == '2':
            menu_secciones()
        elif opcion == '3':
            menu_materias()
        elif opcion == '4':
            menu_maestros()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


### Submenú para Estudiantes
def menu_estudiantes():
    while True:
        print("\nGESTIÓN DE ESTUDIANTES")
        print("1. Agregar estudiante")
        print("2. Ver todos los estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del estudiante: ")
            Estudiante.agregar(nombre)
            print("Estudiante agregado exitosamente.")
        elif opcion == '2':
            estudiantes = Estudiante.obtener_todos()
            if estudiantes:
                print("Estudiantes:")
                for estudiante in estudiantes:
                    print(f"{estudiante[0]} - {estudiante[1]}")
            else:
                print("No hay estudiantes registrados.")
        elif opcion == '3':
            id = input("Ingrese el ID del estudiante a actualizar: ")
            nombre = input("Ingrese el nuevo nombre del estudiante: ")
            try:
                Estudiante.actualizar(id, nombre)
                print("Estudiante actualizado exitosamente.")
            except sqlite3.Error as e:
                print("Error al actualizar el estudiante:", e)
        elif opcion == '4':
            id = input("Ingrese el ID del estudiante a eliminar: ")
            try:
                Estudiante.eliminar(id)
                print("Estudiante eliminado exitosamente.")
            except sqlite3.Error as e:
                print("Error al eliminar el estudiante:", e)
        elif opcion == '5':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

### Submenú para Secciones
def menu_secciones():
    while True:
        print("\nGESTIÓN DE SECCIONES")
        print("1. Agregar sección")
        print("2. Ver todas las secciones")
        print("3. Actualizar sección")
        print("4. Eliminar sección")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre de la nueva sección: ")
            Seccion.agregar(nombre)
            print("Sección agregada exitosamente.")
        elif opcion == '2':
            secciones = Seccion.obtener_todos()
            if secciones:
                print("Secciones:")
                for seccion in secciones:
                    print(f"{seccion[0]} - {seccion[1]}")
            else:
                print("No hay secciones registradas.")
        elif opcion == '3':
            id = input("Ingrese el ID de la sección a actualizar: ")
            nombre = input("Ingrese el nuevo nombre de la sección: ")
            try:
                Seccion.actualizar(id, nombre)
                print("Sección actualizada exitosamente.")
            except Exception as e:
                print(f"Error al actualizar sección: {e}")
        elif opcion == '4':
            id = input("Ingrese el ID de la sección a eliminar: ")
            try:
                Seccion.eliminar(id)
                print("Sección eliminada exitosamente.")
            except Exception as e:
                print(f"Error al eliminar sección: {e}")
        elif opcion == '5':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

### Submenú para Materias
def menu_materias():
    while True:
        print("\nGESTIÓN DE MATERIAS")
        print("1. Agregar materia")
        print("2. Ver todas las materias")
        print("3. Actualizar materia")
        print("4. Eliminar materia")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre de la materia: ")
            duracion_horas = input("Ingrese la duración en horas de la materia: ")
            aula = input("Ingrese el aula donde se imparte: ")
            creditos = input("Ingrese los créditos de la materia: ")
            try:
                Materia.agregar(nombre, int(duracion_horas), aula, int(creditos))
                print("Materia agregada exitosamente.")
            except ValueError:
                print("Error: Por favor, introduzca valores numéricos para duración y créditos.")
            except Exception as e:
                print(f"Error al agregar materia: {e}")

        elif opcion == '2':
            materias = Materia.obtener_todos()
            if materias:
                print("Materias:")
                for materia in materias:
                    print(
                        f"ID: {materia[0]}, Nombre: {materia[1]}, Duración (hrs): {materia[2]}, Aula: {materia[3]}, Créditos: {materia[4]}")
            else:
                print("No hay materias registradas.")

        elif opcion == '3':
            id = input("Ingrese el ID de la materia a actualizar: ")
            nombre = input("Ingrese el nuevo nombre de la materia: ")
            duracion_horas = input("Ingrese la nueva duración en horas de la materia: ")
            aula = input("Ingrese el nuevo aula donde se imparte: ")
            creditos = input("Ingrese los nuevos créditos de la materia: ")
            try:
                Materia.actualizar(id, nombre, int(duracion_horas), aula, int(creditos))
                print("Materia actualizada exitosamente.")
            except ValueError:
                print("Error: Por favor, introduzca valores numéricos para duración y créditos.")
            except Exception as e:
                print(f"Error al actualizar materia: {e}")

        elif opcion == '4':
            id = input("Ingrese el ID de la materia a eliminar: ")
            try:
                Materia.eliminar(id)
                print("Materia eliminada exitosamente.")
            except Exception as e:
                print(f"Error al eliminar materia: {e}")

        elif opcion == '5':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

### Submenú para Maestros
def menu_maestros():
    while True:
        print("\nGESTIÓN DE MAESTROS")
        print("1. Agregar maestro")
        print("2. Ver todos los maestros")
        print("3. Actualizar maestro")
        print("4. Eliminar maestro")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del maestro: ")
            try:
                Maestro.agregar(nombre)
                print("Maestro agregado exitosamente.")
            except Exception as e:
                print(f"Error al agregar maestro: {e}")

        elif opcion == '2':
            maestros = Maestro.obtener_todos()
            if maestros:
                print("Maestros:")
                for maestro in maestros:
                    print(f"ID: {maestro[0]}, Nombre: {maestro[1]}")
            else:
                print("No hay maestros registrados.")

        elif opcion == '3':
            id = input("Ingrese el ID del maestro a actualizar: ")
            nombre = input("Ingrese el nuevo nombre del maestro: ")
            try:
                Maestro.actualizar(id, nombre)
                print("Maestro actualizado exitosamente.")
            except Exception as e:
                print(f"Error al actualizar maestro: {e}")

        elif opcion == '4':
            id = input("Ingrese el ID del maestro a eliminar: ")
            try:
                Maestro.eliminar(id)
                print("Maestro eliminado exitosamente.")
            except Exception as e:
                print(f"Error al eliminar maestro: {e}")

        elif opcion == '5':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    menu_principal()

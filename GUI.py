import tkinter as tk
from tkinter import messagebox
from modelos import Estudiante, Seccion, Materia, Maestro

def main_window():
    window = tk.Tk()
    window.title("Sistema de Inscripción Escolar")

    window.geometry("600x400")

    def agregar_estudiante():
        def guardar_estudiante():
            nombre = entry_nombre.get()
            if nombre:
                try:
                    Estudiante.agregar(nombre)
                    messagebox.showinfo("Éxito", "Estudiante agregado correctamente")
                    add_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"Error al agregar estudiante: {e}")
            else:
                messagebox.showwarning("Advertencia", "El nombre del estudiante es obligatorio")

        add_window = tk.Toplevel()
        add_window.title("Agregar Estudiante")

        tk.Label(add_window, text="Nombre:").grid(row=0, column=0)
        entry_nombre = tk.Entry(add_window)
        entry_nombre.grid(row=0, column=1)

        tk.Button(add_window, text="Guardar", command=guardar_estudiante).grid(row=1, column=0, columnspan=2)

    tk.Button(window, text="Agregar Estudiante", command=agregar_estudiante).pack()

    window.mainloop()

if __name__ == "__main__":
    main_window()

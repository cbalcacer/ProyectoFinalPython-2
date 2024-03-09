import tkinter as tk
from tkinter import messagebox
from modelos import Estudiante, Seccion, Materia, Maestro

def main_window():
    window = tk.Tk()
    window.title("Sistema de Inscripción Escolar")

    window.geometry("600x400")

    window.mainloop()

if __name__ == "__main__":
    main_window()

import sys
import base_datos
from tkinter import *
from tkinter import messagebox

# Intentar importar e inicializar la base de datos
try:
    from base_datos import crear_bd
    crear_bd()
except ImportError as e:
    messagebox.showerror("Error de Importación", f"No se encontró el módulo 'base_datos.py':\n{e}")
except Exception as e:
    messagebox.showerror("Error de Base de Datos", f"Ocurrió un error al inicializar la base de datos:\n{e}")

def abrir_pacientes():
    abrir_pacientes"pacientes")

def abrir_odontologos():
    abrir_odontologos("odontologos")


try:
    root = Tk()
    root.title("Sistema Consultorio Dental")
    root.geometry("400x400")
    root.config(bg="#d9f2ff")

    Label(
        root,
        text="CONSULTORIO DENTAL",
        font=("Arial", 16, "bold"),
        bg="#d9f2ff"
    ).pack(pady=20)

   
    Button(
        root,
        text="Gestión de Pacientes",
        width=25,
        command=abrir_pacientes,
        bg="white"
    ).pack(pady=10)

    Button(
        root,
        text="Gestión de Odontólogos",
        width=25,
        command=abrir_odontologos,
        bg="white"
    ).pack(pady=10)

    Button(
        root,
        text="Salir",
        width=25,
        command=salir,
        bg="red",
        fg="white"
    ).pack(pady=10)

    root.mainloop()

except Exception as e:
    print(f"Error crítico en la interfaz gráfica: {e}")

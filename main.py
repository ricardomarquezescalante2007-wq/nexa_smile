from tkinter import *
from tkinter import ttk, messagebox

from conexion import *
from funciones import *

# Inicializar BD
crear_tablas()

# =========================
# VENTANA PRINCIPAL
# =========================
root = Tk()
root.title("Sistema Consultorio Dental")
root.geometry("750x500")
root.config(bg="#d9f2ff")

# =========================
# FUNCIONES BOTONES
# =========================
def abrir_agregar():
    ventana_agregar()

def abrir_listar():
    ventana_listar()

def salir():
    root.destroy()

# =========================
# TÍTULO
# =========================
Label(root, text="CONSULTORIO DENTAL", font=("Arial", 20, "bold"),
      bg="#d9f2ff").pack(pady=20)

# =========================
# BOTONES PRINCIPALES
# =========================
Button(root, text="Agregar Paciente", width=25, command=abrir_agregar,
       bg="white").pack(pady=10)

Button(root, text="Ver Pacientes", width=25, command=abrir_listar,
       bg="white").pack(pady=10)

Button(root, text="Salir", width=25, command=salir,
       bg="red", fg="white").pack(pady=10)

# =========================
# INICIAR APP
# =========================
root.mainloop()
from tkinter import *
from base_datos import *

# Inicializar BD desde tu archivo existente
crear_bd()

# =========================
# FUNCIONES DE NAVEGACIÓN
# =========================
def abrir_pacientes():
    # Importa y ejecuta el script de pacientes
    import pacientes

def abrir_odontologos():
    import odontologos

def salir():
    root.destroy()

# =========================
# VENTANA PRINCIPAL
# =========================
root = Tk()
root.title("Sistema Consultorio Dental")
root.geometry("400x400")
root.config(bg="#d9f2ff")

Label(root, text="CONSULTORIO DENTAL", font=("Arial", 16, "bold"),
      bg="#d9f2ff").pack(pady=20)

# =========================
# BOTONES
# =========================
Button(root, text="Gestión de Pacientes", width=25, command=abrir_pacientes,
       bg="white").pack(pady=10)

Button(root, text="Gestión de Odontólogos", width=25, command=abrir_odontologos,
       bg="white").pack(pady=10)

Button(root, text="Salir", width=25, command=salir,
       bg="red", fg="white").pack(pady=10)

root.mainloop()
import sys
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
    try:
        # Si el módulo ya fue importado antes, se fuerza su recarga para volver a ejecutar la interfaz
        if "pacientes" in sys.modules:
            import importlib
            importlib.reload(sys.modules["pacientes"])
        else:
            import pacientes
    except ImportError as e:
        messagebox.showerror("Error", f"No se pudo encontrar el archivo 'pacientes.py':\n{e}")
    except Exception as e:
        messagebox.showerror("Error inesperado", f"Ocurrió un problema al abrir Pacientes:\n{e}")

def abrir_odontologos():
    try:
        if "odontologos" in sys.modules:
            import importlib
            importlib.reload(sys.modules["odontologos"])
        else:
            import odontologos
    except ImportError as e:
        messagebox.showerror("Error", f"No se pudo encontrar el archivo 'odontologos.py':\n{e}")
    except Exception as e:
        messagebox.showerror("Error inesperado", f"Ocurrió un problema al abrir Odontólogos:\n{e}")

def salir():
    try:
        root.destroy()
    except Exception as e:
        messagebox.showwarning("Advertencia", f"Error al cerrar la aplicación:\n{e}")


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

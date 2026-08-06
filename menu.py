import sys
import importlib
from tkinter import *
from tkinter import messagebox

def abrir_modulo(nombre_modulo):
    """
    Función genérica para importar o recargar módulos dinámicamente con manejo de errores.
    """
    try:
        if nombre_modulo in sys.modules:
            importlib.reload(sys.modules[nombre_modulo])
        else:
            importlib.import_module(nombre_modulo)
    except ModuleNotFoundError:
        messagebox.showerror(
            "Error de Archivo", 
            f"No se encontró el archivo '{nombre_modulo}.py' en la carpeta del proyecto." 
        )
    except Exception as e:
        messagebox.showerror(
            "Error Inesperado", 
            f"Ocurrió un error al abrir la sección '{nombre_modulo}':\n{e}"
        )

def pacientes():
    abrir_modulo("pacientes")

def odontologos():
    abrir_modulo("odontologos")

def citas():
    abrir_modulo("citas")

def tratamientos():
    abrir_modulo("tratamientos")

def pagos():
    abrir_modulo("pagos")

def abrir_menu():
    try:
        menu = Tk()
        menu.title("Nexa Smile")
        menu.geometry("350x400")
        menu.config(bg="lightblue")

        Label(
            menu,
            text="NEXA SMILE",
            bg="lightblue",
            fg="blue",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

    
        Button(menu, text="👤 Pacientes", width=20, command=pacientes).pack(pady=5)
        Button(menu, text="👨‍⚕️ Odontólogos", width=20, command=odontologos).pack(pady=5)
        Button(menu, text="📅 Citas", width=20, command=citas).pack(pady=5)
        Button(menu, text="🦷 Tratamientos", width=20, command=tratamientos).pack(pady=5)
        Button(menu, text="💳 Pagos", width=20, command=pagos).pack(pady=5)

        Button(
            menu,
            text="Salir",
            width=20,
            bg="red",
            fg="white",
            command=menu.destroy
        ).pack(pady=20)

        menu.mainloop()

    except Exception as e:
        print(f"Error al iniciar el menú principal: {e}")

if __name__ == "__main__":
    abrir_menu()

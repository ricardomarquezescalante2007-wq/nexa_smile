from tkinter import *

# Funciones para abrir los módulos
def pacientes():
    import pacientes

def odontologos():
    import odontologos

def citas():
    import citas

def tratamientos():
    import tratamientos

def pagos():
    import pagos

def abrir_menu():

    menu = Tk()
    menu.title("Nexa Smile")
    menu.geometry("350x400")
    menu.config(bg="lightblue")

    Label(
        menu,
        text="NEXA SMILE",
        bg="lightblue",
        fg="blue",
        font=("Arial",18,"bold")
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
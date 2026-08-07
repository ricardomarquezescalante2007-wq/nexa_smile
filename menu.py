from tkinter import *
from tkinter import messagebox




def pacientes():

    try:
        import pacientes
        pacientes.abrir_ventana()

    except Exception as error:
        messagebox.showerror(
            "Error Pacientes",
            f"No se pudo abrir pacientes:\n\n{error}"
        )



def odontologos():

    try:
        import odontologos
        odontologos.abrir_ventana()

    except Exception as error:
        messagebox.showerror(
            "Error Odontólogos",
            f"No se pudo abrir odontólogos:\n\n{error}"
        )



def citas():

    try:
        import citas
        citas.abrir_ventana()

    except Exception as error:
        messagebox.showerror(
            "Error Citas",
            f"No se pudo abrir citas:\n\n{error}"
        )



def tratamientos():

    try:
        import tratamientos
        tratamientos.abrir_ventana()

    except Exception as error:
        messagebox.showerror(
            "Error Tratamientos",
            f"No se pudo abrir tratamientos:\n\n{error}"
        )



def pagos():

    try:
        import pagos
        pagos.abrir_ventana()

    except Exception as error:
        messagebox.showerror(
            "Error Pagos",
            f"No se pudo abrir pagos:\n\n{error}"
        )



# ======================================
# MENÚ PRINCIPAL
# ======================================

def abrir_menu():

    menu = Tk()

    menu.title("Nexa Smile")
    menu.geometry("350x450")
    menu.config(bg="lightblue")


    Label(
        menu,
        text="NEXA SMILE",
        bg="lightblue",
        fg="blue",
        font=("Arial",18,"bold")
    ).pack(pady=20)



    Button(
        menu,
        text="👤 Pacientes",
        width=20,
        command=pacientes
    ).pack(pady=5)



    Button(
        menu,
        text="👨‍⚕️ Odontólogos",
        width=20,
        command=odontologos
    ).pack(pady=5)



    Button(
        menu,
        text="📅 Citas",
        width=20,
        command=citas
    ).pack(pady=5)



    Button(
        menu,
        text="🦷 Tratamientos",
        width=20,
        command=tratamientos
    ).pack(pady=5)



    Button(
        menu,
        text="💳 Pagos",
        width=20,
        command=pagos
    ).pack(pady=5)



    Button(
        menu,
        text="Salir",
        width=20,
        bg="red",
        fg="white",
        command=menu.destroy
    ).pack(pady=20)



    menu.mainloop()



if __name__ == "__main__":
    abrir_menu()
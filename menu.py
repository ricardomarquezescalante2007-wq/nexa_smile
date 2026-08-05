from tkinter import *
from tkinter import ttk
from pacientes import guardar as guardar_paciente, mostrar as mostrar_paciente
import odontologos as odonto_mod

# VENTANA DE PACIENTES
def pacientes():

    ventana = Toplevel()
    ventana.title("Gestión de Pacientes")
    ventana.geometry("1100x500")

    nombre = StringVar()
    apellido = StringVar()
    fecha = StringVar()
    sexo = StringVar()
    telefono = StringVar()
    correo = StringVar()
    direccion = StringVar()

    frame = Frame(ventana)
    frame.grid(row=0, column=0, padx=20, pady=20)

    Label(frame, text="Nombre").grid(row=0, column=0, sticky=E, pady=5)
    Entry(frame, textvariable=nombre).grid(row=0, column=1)

    Label(frame, text="Apellido").grid(row=1, column=0, sticky=E, pady=5)
    Entry(frame, textvariable=apellido).grid(row=1, column=1)

    Label(frame, text="Fecha Nacimiento").grid(row=2, column=0, sticky=E, pady=5)
    Entry(frame, textvariable=fecha).grid(row=2, column=1)

    Label(frame, text="Sexo").grid(row=3, column=0, sticky=E, pady=5)
    Entry(frame, textvariable=sexo).grid(row=3, column=1)

    Label(frame, text="Teléfono").grid(row=4, column=0, sticky=E, pady=5)
    Entry(frame, textvariable=telefono).grid(row=4, column=1)

    Label(frame, text="Correo").grid(row=5, column=0, sticky=E, pady=5)
    Entry(frame, textvariable=correo).grid(row=5, column=1)

    Label(frame, text="Dirección").grid(row=6, column=0, sticky=E, pady=5)
    Entry(frame, textvariable=direccion).grid(row=6, column=1)

    columnas = (
        "ID",
        "Nombre",
        "Apellido",
        "Fecha Nac.",
        "Sexo",
        "Teléfono",
        "Correo",
        "Dirección",
        "Registro"
    )

    tabla = ttk.Treeview(
        ventana,
        columns=columnas,
        show="headings"
    )

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=100)

    tabla.grid(row=0, column=1, padx=20, pady=20)

    Button(
        frame,
        text="Guardar Paciente",
        bg="green",
        fg="white",
        command=lambda: guardar_paciente(
            nombre,
            apellido,
            fecha,
            sexo,
            telefono,
            correo,
            direccion,
            tabla
        )
    ).grid(row=7, column=0, columnspan=2, pady=20)

    mostrar_paciente(tabla)


# VENTANA DE ODONTOLOGOS 
def odontologos():
    ventana = Toplevel()
    ventana.title("Gestión de Odontólogos")
    ventana.geometry("1100x500")

    nombre = StringVar()
    especialidad = StringVar()
    telefono = StringVar()
    correo = StringVar()
    cedula = StringVar()

    frame = Frame(ventana)
    frame.grid(row=0, column=0, padx=20, pady=20)

    Label(frame, text="Nombre").grid(row=0, column=0, sticky=E, pady=5)
    Entry(frame, textvariable=nombre).grid(row=0, column=1)

    Label(frame, text="Especialidad").grid(row=1, column=0, sticky=E, pady=5)
    Entry(frame, textvariable=especialidad).grid(row=1, column=1)

    Label(frame, text="Teléfono").grid(row=2, column=0, sticky=E, pady=5)
    Entry(frame, textvariable=telefono).grid(row=2, column=1)

    Label(frame, text="Correo").grid(row=3, column=0, sticky=E, pady=5)
    Entry(frame, textvariable=correo).grid(row=3, column=1)

    Label(frame, text="Cédula Profesional").grid(row=4, column=0, sticky=E, pady=5)
    Entry(frame, textvariable=cedula).grid(row=4, column=1)

    columnas = (
        "ID",
        "Nombre",
        "Especialidad",
        "Teléfono",
        "Correo",
        "Cédula Profesional"
    )

    tabla = ttk.Treeview(
        ventana,
        columns=columnas,
        show="headings"
    )

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=150)

    tabla.grid(row=0, column=1, padx=20, pady=20)

    Button(
        frame,
        text="Guardar Odontólogo",
        bg="green",
        fg="white",
        command=lambda: odonto_mod.guardar(
            nombre,
            especialidad,
            telefono,
            correo,
            cedula,
            tabla
        )
    ).grid(row=5, column=0, columnspan=2, pady=20)

    odonto_mod.mostrar(tabla)


def citas():
    import citas


def tratamientos():
    import tratamientos


def pagos():
    import pagos


# MENÚ PRINCIPAL
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
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    Button(menu, text="Pacientes", width=20, command=pacientes).pack(pady=5)
    Button(menu, text="Odontólogos", width=20, command=odontologos).pack(pady=5)
    Button(menu, text="Citas", width=20, command=citas).pack(pady=5)
    Button(menu, text="Tratamientos", width=20, command=tratamientos).pack(pady=5)
    Button(menu, text="Pagos", width=20, command=pagos).pack(pady=5)

    Button(
        menu,
        text="Salir",
        width=20,
        bg="red",
        fg="white",
        command=menu.destroy
    ).pack(pady=20)

    menu.mainloop()


abrir_menu()

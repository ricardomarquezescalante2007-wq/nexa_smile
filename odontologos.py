from tkinter import *
from tkinter import ttk, messagebox
from base_datos import *


# ==========================
# FUNCIONES
# ==========================

def limpiar(nombre, especialidad, telefono, correo, cedula):
    try:
        nombre.set("")
        especialidad.set("")
        telefono.set("")
        correo.set("")
        cedula.set("")

    except Exception as error:
        messagebox.showerror(
            "Error",
            f"No fue posible limpiar los campos.\n\n{error}"
        )



def mostrar(tabla):

    try:

        tabla.delete(*tabla.get_children())

        registros = consultar(
            "SELECT * FROM odontologos"
        )

        for fila in registros:
            tabla.insert(
                "",
                END,
                values=fila
            )


    except Exception as error:

        messagebox.showerror(
            "Error",
            f"No fue posible mostrar los registros.\n\n{error}"
        )



def guardar(nombre, especialidad, telefono, correo, cedula, tabla):

    try:

        if not nombre.get().strip():
            raise ValueError("El nombre es obligatorio.")

        if not especialidad.get().strip():
            raise ValueError("La especialidad es obligatoria.")

        if not telefono.get().strip():
            raise ValueError("El teléfono es obligatorio.")

        if not correo.get().strip():
            raise ValueError("El correo es obligatorio.")

        if not cedula.get().strip():
            raise ValueError("La cédula profesional es obligatoria.")


        ejecutar(
            """
            INSERT INTO odontologos
            (
                nombre,
                especialidad,
                telefono,
                correo,
                cedula_profesional
            )
            VALUES(?,?,?,?,?)
            """,

            (
                nombre.get(),
                especialidad.get(),
                telefono.get(),
                correo.get(),
                cedula.get()
            )
        )


        limpiar(
            nombre,
            especialidad,
            telefono,
            correo,
            cedula
        )


        mostrar(tabla)


        messagebox.showinfo(
            "Éxito",
            "Odontólogo registrado correctamente."
        )


    except ValueError as error:

        messagebox.showwarning(
            "Datos incompletos",
            str(error)
        )


    except Exception as error:

        messagebox.showerror(
            "Error",
            f"Ocurrió un error al guardar.\n\n{error}"
        )



# ==========================
# INTERFAZ
# ==========================

def abrir_ventana():

    ventana = Toplevel()

    ventana.title(
        "Gestión de Odontólogos"
    )

    ventana.geometry(
        "900x500"
    )

    ventana.config(
        bg="#d9f2ff"
    )



    nombre = StringVar()
    especialidad = StringVar()
    telefono = StringVar()
    correo = StringVar()
    cedula = StringVar()



    Label(
        ventana,
        text="Gestión de Odontólogos",
        font=("Arial",16,"bold"),
        bg="#d9f2ff"
    ).pack(
        pady=10
    )



    frame = Frame(
        ventana,
        bg="#d9f2ff"
    )

    frame.pack(
        pady=10
    )



    Label(frame,text="Nombre",bg="#d9f2ff").grid(
        row=0,column=0,padx=5,pady=5
    )

    Entry(
        frame,
        textvariable=nombre,
        width=30
    ).grid(
        row=0,column=1
    )



    Label(frame,text="Especialidad",bg="#d9f2ff").grid(
        row=1,column=0,padx=5,pady=5
    )

    Entry(
        frame,
        textvariable=especialidad,
        width=30
    ).grid(
        row=1,column=1
    )



    Label(frame,text="Teléfono",bg="#d9f2ff").grid(
        row=2,column=0,padx=5,pady=5
    )

    Entry(
        frame,
        textvariable=telefono,
        width=30
    ).grid(
        row=2,column=1
    )



    Label(frame,text="Correo",bg="#d9f2ff").grid(
        row=3,column=0,padx=5,pady=5
    )

    Entry(
        frame,
        textvariable=correo,
        width=30
    ).grid(
        row=3,column=1
    )



    Label(frame,text="Cédula Profesional",bg="#d9f2ff").grid(
        row=4,column=0,padx=5,pady=5
    )

    Entry(
        frame,
        textvariable=cedula,
        width=30
    ).grid(
        row=4,column=1
    )



    tabla = ttk.Treeview(

        ventana,

        columns=(
            "id",
            "nombre",
            "especialidad",
            "telefono",
            "correo",
            "cedula"
        ),

        show="headings",
        height=10
    )



    for columna, titulo in [

        ("id","ID"),
        ("nombre","Nombre"),
        ("especialidad","Especialidad"),
        ("telefono","Teléfono"),
        ("correo","Correo"),
        ("cedula","Cédula")

    ]:

        tabla.heading(
            columna,
            text=titulo
        )



    tabla.column("id",width=50)
    tabla.column("nombre",width=150)
    tabla.column("especialidad",width=150)
    tabla.column("telefono",width=120)
    tabla.column("correo",width=180)
    tabla.column("cedula",width=150)



    tabla.pack(
        pady=10,
        fill="both",
        expand=True
    )



    Button(

        ventana,

        text="Guardar",

        bg="green",

        fg="white",

        width=20,

        command=lambda: guardar(
            nombre,
            especialidad,
            telefono,
            correo,
            cedula,
            tabla
        )

    ).pack(
        pady=10
    )



    mostrar(tabla)
from tkinter import *
from tkinter import ttk, messagebox
from base_datos import *

# ==========================================
# COLORES DE LA INTERFAZ
# ==========================================

COLOR_FONDO = "#27FBFF"
COLOR_LILA = "#8D3EDD"
COLOR_LILA_HOVER = "#983DEE"
COLOR_TEXTO_BOTON = "#3B0764"
COLOR_PANEL = "#F0F9FF"


# ==========================================
# LIMPIAR CAMPOS
# ==========================================

def limpiar(nombre, apellido, fecha, sexo, telefono, correo, direccion):

    try:
        nombre.set("")
        apellido.set("")
        fecha.set("")
        sexo.set("")
        telefono.set("")
        correo.set("")
        direccion.set("")

    except Exception as error:

        messagebox.showerror(
            "Error",
            f"No fue posible limpiar los campos.\n\n{error}"
        )


# ==========================================
# MOSTRAR PACIENTES
# ==========================================

def mostrar(tabla):

    try:

        tabla.delete(*tabla.get_children())

        registros = consultar(
            "SELECT * FROM pacientes"
        )

        for fila in registros:

            tabla.insert(
                "",
                "end",
                values=fila
            )


    except Exception as error:

        messagebox.showerror(
            "Error",
            f"No fue posible mostrar los registros.\n\n{error}"
        )


# ==========================================
# GUARDAR PACIENTE
# ==========================================

def guardar(
    nombre,
    apellido,
    fecha,
    sexo,
    telefono,
    correo,
    direccion,
    tabla
):

    try:

        if not nombre.get().strip():
            raise ValueError("El nombre es obligatorio.")

        if not apellido.get().strip():
            raise ValueError("El apellido es obligatorio.")

        if not fecha.get().strip():
            raise ValueError("La fecha de nacimiento es obligatoria.")

        if not sexo.get().strip():
            raise ValueError("El sexo es obligatorio.")

        if not telefono.get().strip():
            raise ValueError("El teléfono es obligatorio.")

        if not correo.get().strip():
            raise ValueError("El correo es obligatorio.")

        if not direccion.get().strip():
            raise ValueError("La dirección es obligatoria.")



        ejecutar(
            """
            INSERT INTO pacientes(
                nombre,
                apellido,
                fecha_nacimiento,
                sexo,
                telefono,
                correo,
                direccion,
                fecha_registro
            )
            VALUES(?,?,?,?,?,?,?,?)
            """,

            (
                nombre.get(),
                apellido.get(),
                fecha.get(),
                sexo.get(),
                telefono.get(),
                correo.get(),
                direccion.get(),
                "2026-06-26"
            )
        )


        limpiar(
            nombre,
            apellido,
            fecha,
            sexo,
            telefono,
            correo,
            direccion
        )


        mostrar(tabla)


        messagebox.showinfo(
            "Éxito",
            "Paciente registrado correctamente."
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



# ==========================================
# INTERFAZ DE PACIENTES
# ==========================================

def abrir_ventana():

    ventana = Toplevel()

    ventana.title(
        "Nexa Smile - Pacientes"
    )

    ventana.geometry(
        "950x600"
    )

    ventana.config(
        bg=COLOR_FONDO
    )


    # Estilo tabla

    estilo = ttk.Style()

    estilo.configure(
        "Treeview",
        background="white",
        foreground=COLOR_TEXTO_BOTON,
        rowheight=30,
        fieldbackground="white"
    )

    estilo.configure(
        "Treeview.Heading",
        background=COLOR_LILA,
        foreground="white",
        font=("Arial",10,"bold")
    )


    # Variables

    nombre = StringVar()
    apellido = StringVar()
    fecha = StringVar()
    sexo = StringVar()
    telefono = StringVar()
    correo = StringVar()
    direccion = StringVar()



    # Título

    Label(
        ventana,
        text="Registro de Pacientes",
        font=("Arial",18,"bold"),
        bg=COLOR_FONDO,
        fg=COLOR_LILA
    ).pack(
        pady=15
    )



    # Frame formulario

    formulario = Frame(
        ventana,
        bg=COLOR_PANEL
    )

    formulario.pack()



    datos = [

        ("Nombre", nombre),
        ("Apellido", apellido),
        ("Fecha nacimiento", fecha),
        ("Sexo", sexo),
        ("Teléfono", telefono),
        ("Correo", correo),
        ("Dirección", direccion)

    ]



    for fila, (texto, variable) in enumerate(datos):

        Label(
            formulario,
            text=texto,
            bg=COLOR_PANEL,
            fg=COLOR_TEXTO_BOTON,
            font=("Arial",10,"bold")
        ).grid(
            row=fila,
            column=0,
            padx=10,
            pady=5
        )


        Entry(
            formulario,
            textvariable=variable,
            width=40,
            bg="white",
            fg=COLOR_TEXTO_BOTON
        ).grid(
            row=fila,
            column=1,
            padx=10,
            pady=5
        )



    # Tabla

    tabla = ttk.Treeview(

        ventana,

        columns=(

            "ID",
            "Nombre",
            "Apellido",
            "Nacimiento",
            "Sexo",
            "Telefono",
            "Correo",
            "Direccion",
            "Registro"

        ),

        show="headings"

    )



    for columna in tabla["columns"]:

        tabla.heading(
            columna,
            text=columna
        )

        tabla.column(
            columna,
            width=90
        )



    tabla.pack(

        expand=True,

        fill="both",

        pady=15

    )



    # Botones

    botones = Frame(
        ventana,
        bg=COLOR_FONDO
    )

    botones.pack()



    Button(
        botones,
        text="Guardar",
        width=15,
        bg=COLOR_LILA,
        fg="white",
        activebackground=COLOR_LILA_HOVER,
        activeforeground="white",
        font=("Arial",10,"bold"),
        command=lambda: guardar(
            nombre,
            apellido,
            fecha,
            sexo,
            telefono,
            correo,
            direccion,
            tabla
        )
    ).grid(
        row=0,
        column=0,
        padx=10
    )



    Button(
        botones,
        text="Limpiar",
        width=15,
        bg=COLOR_LILA,
        fg="white",
        activebackground=COLOR_LILA_HOVER,
        activeforeground="white",
        font=("Arial",10,"bold"),
        command=lambda: limpiar(
            nombre,
            apellido,
            fecha,
            sexo,
            telefono,
            correo,
            direccion
        )

    ).grid(
        row=0,
        column=1,
        padx=10
    )



    Button(
        botones,
        text="Actualizar",
        width=15,
        bg=COLOR_LILA,
        fg="white",
        activebackground=COLOR_LILA_HOVER,
        activeforeground="white",
        font=("Arial",10,"bold"),
        command=lambda: mostrar(tabla)

    ).grid(
        row=0,
        column=2,
        padx=10
    )



    # Cargar datos iniciales

    mostrar(tabla)


    ventana.mainloop()
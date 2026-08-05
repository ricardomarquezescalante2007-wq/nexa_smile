from tkinter import messagebox
from base_datos import *

# FUNCIÓN PARA LIMPIAR LOS CAMPOS DEL FORMULARIO
def limpiar(nombre, especialidad, telefono, correo, cedula):
    try:
        # Limpia el contenido de cada campo
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

# FUNCIÓN PARA MOSTRAR LOS ODONTÓLOGOS
def mostrar(tabla):
    try:
        # Elimina los registros actuales del Treeview
        tabla.delete(*tabla.get_children())

        # Consulta todos los odontólogos
        registros = consultar("SELECT * FROM odontologos")

        # Agrega los registros a la tabla
        for fila in registros:
            tabla.insert("", "end", values=fila)

    except Exception as error:
        messagebox.showerror(
            "Error",
            f"No fue posible mostrar los registros.\n\n{error}"
        )


# FUNCIÓN PARA GUARDAR UN ODONTÓLOGO
def guardar(nombre, especialidad, telefono, correo, cedula, tabla):

    try:
        # VALIDACIONES

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

        # INSERTA EL REGISTRO

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

        # Limpia los campos
        limpiar(
            nombre,
            especialidad,
            telefono,
            correo,
            cedula
        )

        # Actualiza la tabla
        mostrar(tabla)

        # Mensaje de éxito
        messagebox.showinfo(
            "Éxito",
            "Odontólogo registrado correctamente."
        )

    # Captura errores de validación
    except ValueError as error:

        messagebox.showwarning(
            "Datos incompletos",
            str(error)
        )

    # Captura cualquier otro error
    except Exception as error:

        messagebox.showerror(
            "Error",
            f"Ocurrió un error al guardar.\n\n{error}"
        )

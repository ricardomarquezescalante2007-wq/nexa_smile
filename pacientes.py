from tkinter import messagebox
from base_datos import *

# FUNCIÓN PARA LIMPIAR LOS CAMPOS
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


# FUNCIÓN PARA MOSTRAR LOS REGISTROS
def mostrar(tabla):
    try:
        # Borra todos los registros del Treeview
        tabla.delete(*tabla.get_children())

        # Consulta la base de datos
        registros = consultar("SELECT * FROM pacientes")

        # Agrega los registros al Treeview
        for fila in registros:
            tabla.insert("", "end", values=fila)

    except Exception as error:
        messagebox.showerror(
            "Error",
            f"No fue posible mostrar los registros.\n\n{error}"
        )


# FUNCIÓN PARA GUARDAR UN PACIENTE
def guardar(nombre, apellido, fecha, sexo, telefono, correo, direccion, tabla):

    try:

        # Validaciones
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

        # Guarda el paciente en la base de datos
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

        # Limpia el formulario
        limpiar(
            nombre,
            apellido,
            fecha,
            sexo,
            telefono,
            correo,
            direccion
        )

        # Actualiza la tabla
        mostrar(tabla)

        # Mensaje de éxito
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

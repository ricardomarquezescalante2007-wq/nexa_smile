import tkinter as tk
from tkinter import ttk, messagebox
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
                specialidad,
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

# INTERFAZ GRÁFICA
root = tk.Tk()
root.title("Gestión de Odontólogos")
root.geometry("700x500")

nombre_var = tk.StringVar()
especialidad_var = tk.StringVar()
telefono_var = tk.StringVar()
correo_var = tk.StringVar()
cedula_var = tk.StringVar()

frame_form = tk.LabelFrame(root, text="Datos del Odontólogo")
frame_form.pack(fill="x", padx=10, pady=10)

tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
tk.Entry(frame_form, textvariable=nombre_var, width=30).grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Especialidad:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
tk.Entry(frame_form, textvariable=especialidad_var, width=30).grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Teléfono:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
tk.Entry(frame_form, textvariable=telefono_var, width=30).grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Correo:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
tk.Entry(frame_form, textvariable=correo_var, width=30).grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Cédula Profesional:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
tk.Entry(frame_form, textvariable=cedula_var, width=30).grid(row=4, column=1, padx=5, pady=5)

frame_botones = tk.Frame(root)
frame_botones.pack(fill="x", padx=10, pady=5)

btn_guardar = tk.Button(frame_botones, text="Guardar", command=lambda: guardar(nombre_var, especialidad_var, telefono_var, correo_var, cedula_var, tabla))
btn_guardar.pack(side="left", padx=5)

btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=lambda: limpiar(nombre_var, especialidad_var, telefono_var, correo_var, cedula_var))
btn_limpiar.pack(side="left", padx=5)

frame_tabla = tk.Frame(root)
frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

columnas = ("ID", "Nombre", "Especialidad", "Teléfono", "Correo", "Cédula")
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=100)

tabla.pack(fill="both", expand=True)

mostrar(tabla)

root.mainloop()

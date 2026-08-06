import tkinter as tk
from tkinter import ttk, messagebox
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

# INTERFAZ GRÁFICA
root = tk.Tk()
root.title("Gestión de Pacientes")
root.geometry("850x600")

nombre_var = tk.StringVar()
apellido_var = tk.StringVar()
fecha_var = tk.StringVar()
sexo_var = tk.StringVar()
telefono_var = tk.StringVar()
correo_var = tk.StringVar()
direccion_var = tk.StringVar()

frame_form = tk.LabelFrame(root, text="Datos del Paciente")
frame_form.pack(fill="x", padx=10, pady=10)

campos = [
    ("Nombre:", nombre_var),
    ("Apellido:", apellido_var),
    ("Fecha Nacimiento (YYYY-MM-DD):", fecha_var),
    ("Sexo:", sexo_var),
    ("Teléfono:", telefono_var),
    ("Correo:", correo_var),
    ("Dirección:", direccion_var)
]

for i, (texto, variable) in enumerate(campos):
    tk.Label(frame_form, text=texto).grid(row=i, column=0, sticky="w", padx=5, pady=2)
    tk.Entry(frame_form, textvariable=variable, width=40).grid(row=i, column=1, padx=5, pady=2)

frame_botones = tk.Frame(root)
frame_botones.pack(fill="x", padx=10, pady=5)

btn_guardar = tk.Button(frame_botones, text="Guardar", command=lambda: guardar(nombre_var, apellido_var, fecha_var, sexo_var, telefono_var, correo_var, direccion_var, tabla))
btn_guardar.pack(side="left", padx=5)

btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=lambda: limpiar(nombre_var, apellido_var, fecha_var, sexo_var, telefono_var, correo_var, direccion_var))
btn_limpiar.pack(side="left", padx=5)

frame_tabla = tk.Frame(root)
frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

columnas = ("ID", "Nombre", "Apellido", "Fecha Nac.", "Sexo", "Teléfono", "Correo", "Dirección", "Registro")
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=90)

tabla.pack(fill="both", expand=True)

mostrar(tabla)

root.mainloop()

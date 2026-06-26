from tkinter import *
from tkinter import ttk
from base_datos import *

crear_bd()

# =====================
# FUNCIONES
# =====================

def guardar():
    ejecutar("""
    INSERT INTO odontologos(nombre,especialidad,telefono)
    VALUES(?,?,?)
    """,(nombre.get(),especialidad.get(),telefono.get()))

    limpiar()
    mostrar()


def mostrar():
    tabla.delete(*tabla.get_children())

    datos = consultar("SELECT * FROM odontologos")

    for fila in datos:
        tabla.insert("", END, values=fila)


def eliminar():
    if tabla.selection():

        id = tabla.item(tabla.selection())["values"][0]

        ejecutar(
            "DELETE FROM odontologos WHERE id_odontologo=?",
            (id,)
        )

        mostrar()


def seleccionar(event):
    if tabla.selection():

        datos = tabla.item(tabla.selection())["values"]

        nombre.set(datos[1])
        especialidad.set(datos[2])
        telefono.set(datos[3])


def actualizar():
    if tabla.selection():

        id = tabla.item(tabla.selection())["values"][0]

        ejecutar("""
        UPDATE odontologos
        SET nombre=?, especialidad=?, telefono=?
        WHERE id_odontologo=?
        """,(nombre.get(),
             especialidad.get(),
             telefono.get(),
             id))

        limpiar()
        mostrar()


def limpiar():
    nombre.set("")
    especialidad.set("")
    telefono.set("")


# =====================
# VENTANA
# =====================

ventana = Tk()
ventana.title("Odontólogos")
ventana.geometry("700x450")
ventana.config(bg="lightblue")

nombre = StringVar()
especialidad = StringVar()
telefono = StringVar()

Label(ventana, text="Nombre", bg="lightblue").place(x=20, y=20)
Entry(ventana, textvariable=nombre).place(x=120, y=20)

Label(ventana, text="Especialidad", bg="lightblue").place(x=20, y=60)
Entry(ventana, textvariable=especialidad).place(x=120, y=60)

Label(ventana, text="Teléfono", bg="lightblue").place(x=20, y=100)
Entry(ventana, textvariable=telefono).place(x=120, y=100)

Button(ventana, text="Guardar", bg="green", fg="white",
       command=guardar).place(x=350, y=20)

Button(ventana, text="Actualizar", bg="blue", fg="white",
       command=actualizar).place(x=350, y=60)

Button(ventana, text="Eliminar", bg="red", fg="white",
       command=eliminar).place(x=350, y=100)

tabla = ttk.Treeview(
    ventana,
    columns=(1,2,3,4,5,6),
    show="headings",
    height=10
)

tabla.heading(1, text="ID")
tabla.heading(2, text="Nombre")
tabla.heading(3, text="Especialidad")
tabla.heading(4, text="Teléfono")
tabla.heading(5, text="Correo")
tabla.heading(6, text="Cédula")

tabla.column(1, width=50)

tabla.pack(side=BOTTOM, fill=X, pady=20)

tabla.bind("<ButtonRelease-1>", seleccionar)

mostrar()

ventana.mainloop()
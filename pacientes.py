from tkinter import *
from tkinter import ttk, messagebox
from base_datos import *

crear_bd()

# ======================
# FUNCIONES
# ======================

def guardar():
    ejecutar("""
    INSERT INTO pacientes(nombre,apellido,telefono)
    VALUES(?,?,?)
    """,(nombre.get(),apellido.get(),telefono.get()))

    limpiar()
    mostrar()


def mostrar():
    tabla.delete(*tabla.get_children())

    datos = consultar("SELECT * FROM pacientes")

    for fila in datos:
        tabla.insert("",END,values=fila)


def eliminar():
    if tabla.selection():

        id = tabla.item(tabla.selection())["values"][0]

        ejecutar("DELETE FROM pacientes WHERE id_paciente=?",(id,))

        mostrar()


def seleccionar(event):

    fila = tabla.item(tabla.selection())

    datos = fila["values"]

    nombre.set(datos[1])
    apellido.set(datos[2])
    telefono.set(datos[5])


def actualizar():

    if tabla.selection():

        id = tabla.item(tabla.selection())["values"][0]

        ejecutar("""
        UPDATE pacientes
        SET nombre=?,apellido=?,telefono=?
        WHERE id_paciente=?
        """,(nombre.get(),
             apellido.get(),
             telefono.get(),
             id))

        limpiar()
        mostrar()


def limpiar():

    nombre.set("")
    apellido.set("")
    telefono.set("")


# ======================
# VENTANA
# ======================

ventana = Tk()
ventana.title("Pacientes")
ventana.geometry("700x450")
ventana.config(bg="lightblue")

nombre = StringVar()
apellido = StringVar()
telefono = StringVar()

Label(ventana,text="Nombre",bg="lightblue").place(x=20,y=20)
Entry(ventana,textvariable=nombre).place(x=100,y=20)

Label(ventana,text="Apellido",bg="lightblue").place(x=20,y=60)
Entry(ventana,textvariable=apellido).place(x=100,y=60)

Label(ventana,text="Teléfono",bg="lightblue").place(x=20,y=100)
Entry(ventana,textvariable=telefono).place(x=100,y=100)

Button(ventana,text="Guardar",command=guardar,bg="green",fg="white").place(x=350,y=20)
Button(ventana,text="Actualizar",command=actualizar,bg="blue",fg="white").place(x=350,y=60)
Button(ventana,text="Eliminar",command=eliminar,bg="red",fg="white").place(x=350,y=100)

tabla = ttk.Treeview(
    ventana,
    columns=(1,2,3,4,5,6,7,8),
    show="headings",
    height=10
)

tabla.heading(1,text="ID")
tabla.heading(2,text="Nombre")
tabla.heading(3,text="Apellido")
tabla.heading(4,text="Nacimiento")
tabla.heading(5,text="Sexo")
tabla.heading(6,text="Teléfono")
tabla.heading(7,text="Correo")
tabla.heading(8,text="Dirección")

tabla.column(1,width=40)
tabla.pack(side=BOTTOM,fill=X,pady=20)

tabla.bind("<ButtonRelease-1>",seleccionar)

mostrar()

ventana.mainloop()
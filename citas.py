from tkinter import *
from tkinter import ttk
from base_datos import *

crear_bd()

# ==========================
# FUNCIONES
# ==========================

def cargar():
    pacientes["values"] = [f"{i[0]} - {i[1]}" for i in consultar("SELECT id_paciente,nombre FROM pacientes")]
    odontologos["values"] = [f"{i[0]} - {i[1]}" for i in consultar("SELECT id_odontologo,nombre FROM odontologos")]

def guardar():

    id_paciente = pacientes.get().split(" - ")[0]
    id_odontologo = odontologos.get().split(" - ")[0]

    ejecutar("""
    INSERT INTO citas
    (id_paciente,id_odontologo,fecha,hora,motivo,estado)
    VALUES(?,?,?,?,?,?)
    """,(id_paciente,id_odontologo,
         fecha.get(),
         hora.get(),
         motivo.get(),
         estado.get()))

    mostrar()

def mostrar():

    tabla.delete(*tabla.get_children())

    datos = consultar("SELECT * FROM citas")

    for fila in datos:
        tabla.insert("",END,values=fila)

def eliminar():

    if tabla.selection():

        id = tabla.item(tabla.selection())["values"][0]

        ejecutar("DELETE FROM citas WHERE id_cita=?",(id,))

        mostrar()


# ==========================
# VENTANA
# ==========================

ventana = Tk()
ventana.title("Citas")
ventana.geometry("750x450")
ventana.config(bg="lightblue")

Label(ventana,text="Paciente",bg="lightblue").place(x=20,y=20)
pacientes = ttk.Combobox(ventana,width=25)
pacientes.place(x=100,y=20)

Label(ventana,text="Odontólogo",bg="lightblue").place(x=20,y=60)
odontologos = ttk.Combobox(ventana,width=25)
odontologos.place(x=100,y=60)

Label(ventana,text="Fecha",bg="lightblue").place(x=20,y=100)
fecha = Entry(ventana)
fecha.place(x=100,y=100)

Label(ventana,text="Hora",bg="lightblue").place(x=20,y=140)
hora = Entry(ventana)
hora.place(x=100,y=140)

Label(ventana,text="Motivo",bg="lightblue").place(x=20,y=180)
motivo = Entry(ventana)
motivo.place(x=100,y=180)

Label(ventana,text="Estado",bg="lightblue").place(x=20,y=220)
estado = ttk.Combobox(ventana,
                      values=["Pendiente","Confirmada","Cancelada"])
estado.place(x=100,y=220)
estado.current(0)

Button(ventana,text="Guardar",bg="green",
fg="white",command=guardar).place(x=380,y=30)

Button(ventana,text="Eliminar",bg="red",
fg="white",command=eliminar).place(x=380,y=80)

tabla = ttk.Treeview(
    ventana,
    columns=(1,2,3,4,5,6,7),
    show="headings",
    height=8
)

tabla.heading(1,text="ID")
tabla.heading(2,text="Paciente")
tabla.heading(3,text="Odontólogo")
tabla.heading(4,text="Fecha")
tabla.heading(5,text="Hora")
tabla.heading(6,text="Motivo")
tabla.heading(7,text="Estado")

tabla.pack(side=BOTTOM,fill=X,pady=20)

cargar()
mostrar()

ventana.mainloop()
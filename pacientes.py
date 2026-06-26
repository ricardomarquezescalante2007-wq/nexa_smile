from tkinter import *
from tkinter import ttk, messagebox
from base_datos import *

# Función para guardar datos
def guardar():
    if not nombre.get():
        messagebox.showwarning("Error", "El nombre es obligatorio")
        return
    
    ejecutar("""
    INSERT INTO pacientes(nombre, apellido, fecha_nacimiento, sexo, telefono, correo, direccion, fecha_registro)
    VALUES(?,?,?,?,?,?,?,?)
    """, (nombre.get(), apellido.get(), fecha.get(), sexo.get(), telefono.get(), correo.get(), direccion.get(), "2026-06-26"))
    limpiar()
    mostrar()
    messagebox.showinfo("Éxito", "Paciente registrado correctamente")

# Función para mostrar datos en la tabla
def mostrar():
    tabla.delete(*tabla.get_children())
    for fila in consultar("SELECT * FROM pacientes"):
        tabla.insert("", END, values=fila)

def limpiar():
    for var in [nombre, apellido, fecha, sexo, telefono, correo, direccion]:
        var.set("")

# Configuración de ventana
ventana = Tk()
ventana.title("Gestión de Pacientes")
ventana.geometry("1100x500")

# Variables
nombre = StringVar(); apellido = StringVar(); fecha = StringVar(); sexo = StringVar()
telefono = StringVar(); correo = StringVar(); direccion = StringVar()

# Formulario (Lado izquierdo usando grid)
frame_form = Frame(ventana)
frame_form.grid(row=0, column=0, padx=20, pady=20, sticky="n")

campos = [("Nombre", nombre), ("Apellido", apellido), ("Fecha Nac.", fecha), 
          ("Sexo", sexo), ("Teléfono", telefono), ("Correo", correo), ("Dirección", direccion)]

for i, (texto, var) in enumerate(campos):
    Label(frame_form, text=texto).grid(row=i, column=0, sticky="e", padx=5, pady=5)
    Entry(frame_form, textvariable=var).grid(row=i, column=1, padx=5, pady=5)

Button(frame_form, text="Guardar Paciente", command=guardar, bg="green", fg="white").grid(row=8, column=0, columnspan=2, pady=20)

# Tabla (Lado derecho)
columnas = ("ID", "Nombre", "Apellido", "F. Nac", "Sexo", "Tel", "Correo", "Dir", "Registro")
tabla = ttk.Treeview(ventana, columns=columnas, show="headings")

for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=90)

tabla.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

mostrar()
ventana.mainloop()
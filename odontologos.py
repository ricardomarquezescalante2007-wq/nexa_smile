from tkinter import *
from tkinter import ttk, messagebox
from base_datos import *

def guardar():
    if not nombre.get():
        messagebox.showwarning("Error", "El nombre es obligatorio")
        return
    
    ejecutar("""
    INSERT INTO odontologos(nombre, especialidad, telefono, correo, cedula_profesional)
    VALUES(?,?,?,?,?)
    """, (nombre.get(), especialidad.get(), telefono.get(), correo.get(), cedula.get()))
    limpiar()
    mostrar()
    messagebox.showinfo("Éxito", "Odontólogo registrado")

def mostrar():
    tabla.delete(*tabla.get_children())
    for fila in consultar("SELECT * FROM odontologos"):
        tabla.insert("", END, values=fila)

def limpiar():
    for var in [nombre, especialidad, telefono, correo, cedula]:
        var.set("")

# Configuración de ventana
ventana = Tk()
ventana.title("Gestión de Odontólogos")
ventana.geometry("1100x500")

# Variables
nombre = StringVar(); especialidad = StringVar(); telefono = StringVar()
correo = StringVar(); cedula = StringVar()

# Formulario
frame_form = Frame(ventana)
frame_form.grid(row=0, column=0, padx=20, pady=20, sticky="n")

campos = [("Nombre", nombre), ("Especialidad", especialidad), ("Teléfono", telefono), 
          ("Correo", correo), ("Cédula Prof.", cedula)]

for i, (texto, var) in enumerate(campos):
    Label(frame_form, text=texto).grid(row=i, column=0, sticky="e", padx=5, pady=5)
    Entry(frame_form, textvariable=var).grid(row=i, column=1, padx=5, pady=5)

Button(frame_form, text="Guardar Odontólogo", command=guardar, bg="green", fg="white").grid(row=6, column=0, columnspan=2, pady=20)

# Tabla
columnas = ("ID", "Nombre", "Especialidad", "Tel", "Correo", "Cédula")
tabla = ttk.Treeview(ventana, columns=columnas, show="headings")

for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=100)

tabla.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

mostrar()
ventana.mainloop()
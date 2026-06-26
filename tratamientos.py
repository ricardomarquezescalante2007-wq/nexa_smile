from tkinter import *
from tkinter import ttk, messagebox
from base_datos import *

def cargar_pacientes():
    # Carga los pacientes en el combo
    pacientes["values"] = [f"{i[0]} - {i[1]} {i[2]}" for i in consultar("SELECT id_paciente, nombre, apellido FROM pacientes")]

def guardar():
    if not nombre.get() or not pacientes.get():
        messagebox.showwarning("Error", "El nombre del tratamiento y el paciente son obligatorios")
        return
    
    id_pac = pacientes.get().split(" - ")[0]
    ejecutar("""
    INSERT INTO tratamientos(id_paciente, nombre_tratamiento, descripcion, costo, fecha_inicio, fecha_fin)
    VALUES(?,?,?,?,?,?)
    """, (id_pac, nombre.get(), desc.get(), costo.get(), f_inicio.get(), f_fin.get()))
    
    limpiar()
    mostrar()
    messagebox.showinfo("Éxito", "Tratamiento registrado")

def mostrar():
    tabla.delete(*tabla.get_children())
    for fila in consultar("SELECT * FROM tratamientos"):
        tabla.insert("", END, values=fila)

def limpiar():
    pacientes.set(""); nombre.set(""); desc.set(""); costo.set(""); f_inicio.set(""); f_fin.set("")

# Configuración de ventana
ventana = Tk()
ventana.title("Gestión de Tratamientos")
ventana.geometry("1000x500")

# Variables
nombre = StringVar(); desc = StringVar(); costo = StringVar(); f_inicio = StringVar(); f_fin = StringVar()

# Formulario
frame_form = Frame(ventana)
frame_form.grid(row=0, column=0, padx=20, pady=20, sticky="n")

Label(frame_form, text="Paciente").grid(row=0, column=0, sticky="e")
pacientes = ttk.Combobox(frame_form, width=25, state="readonly")
pacientes.grid(row=0, column=1, pady=5)

campos = [("Nombre Tratamiento", nombre), ("Descripción", desc), ("Costo", costo), 
          ("F. Inicio", f_inicio), ("F. Fin", f_fin)]

for i, (texto, var) in enumerate(campos, 1):
    Label(frame_form, text=texto).grid(row=i, column=0, sticky="e", padx=5, pady=5)
    Entry(frame_form, textvariable=var).grid(row=i, column=1, padx=5, pady=5)

Button(frame_form, text="Guardar Tratamiento", command=guardar, bg="green", fg="white").grid(row=6, column=0, columnspan=2, pady=20)

# Tabla
columnas = ("ID", "ID Pac", "Nombre", "Desc", "Costo", "Inicio", "Fin")
tabla = ttk.Treeview(ventana, columns=columnas, show="headings")

for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=100)

tabla.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

cargar_pacientes()
mostrar()
ventana.mainloop()
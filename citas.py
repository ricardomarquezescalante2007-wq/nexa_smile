from tkinter import *
from tkinter import ttk, messagebox
from base_datos import *

# Funciones de lógica
def cargar_combos():
    pacientes["values"] = [f"{i[0]} - {i[1]}" for i in consultar("SELECT id_paciente, nombre FROM pacientes")]
    odontologos["values"] = [f"{i[0]} - {i[1]}" for i in consultar("SELECT id_odontologo, nombre FROM odontologos")]

def guardar():
    if not fecha.get() or not pacientes.get():
        messagebox.showwarning("Error", "Completa los campos obligatorios")
        return
    
    id_pac = pacientes.get().split(" - ")[0]
    id_odonto = odontologos.get().split(" - ")[0]
    
    ejecutar("""
    INSERT INTO citas(id_paciente, id_odontologo, fecha, hora, motivo, estado)
    VALUES(?,?,?,?,?,?)
    """, (id_pac, id_odonto, fecha.get(), hora.get(), motivo.get(), estado.get()))
    
    limpiar()
    mostrar()
    messagebox.showinfo("Éxito", "Cita registrada")

def mostrar():
    tabla.delete(*tabla.get_children())
    for fila in consultar("SELECT * FROM citas"):
        tabla.insert("", END, values=fila)

def limpiar():
    fecha.set(""); hora.set(""); motivo.set(""); estado.set("")

# Configuración de ventana
ventana = Tk()
ventana.title("Gestión de Citas")
ventana.geometry("900x500")

# Variables
fecha = StringVar(); hora = StringVar(); motivo = StringVar(); estado = StringVar()

# Formulario
frame_form = Frame(ventana)
frame_form.grid(row=0, column=0, padx=20, pady=20, sticky="n")

Label(frame_form, text="Paciente").grid(row=0, column=0, sticky="e")
pacientes = ttk.Combobox(frame_form, width=25, state="readonly")
pacientes.grid(row=0, column=1, pady=5)

Label(frame_form, text="Odontólogo").grid(row=1, column=0, sticky="e")
odontologos = ttk.Combobox(frame_form, width=25, state="readonly")
odontologos.grid(row=1, column=1, pady=5)

campos = [("Fecha", fecha), ("Hora", hora), ("Motivo", motivo)]
for i, (texto, var) in enumerate(campos, 2):
    Label(frame_form, text=texto).grid(row=i, column=0, sticky="e")
    Entry(frame_form, textvariable=var).grid(row=i, column=1, pady=5)

Label(frame_form, text="Estado").grid(row=5, column=0, sticky="e")
estado = ttk.Combobox(frame_form, values=["Pendiente", "Confirmada", "Cancelada"], width=23)
estado.grid(row=5, column=1, pady=5)

Button(frame_form, text="Guardar Cita", command=guardar, bg="green", fg="white").grid(row=6, column=0, columnspan=2, pady=20)

# Tabla
columnas = ("ID", "ID Pac", "ID Odon", "Fecha", "Hora", "Motivo", "Estado")
tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=100)

tabla.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

cargar_combos()
mostrar()
ventana.mainloop()
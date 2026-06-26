from tkinter import *
from tkinter import ttk, messagebox
from base_datos import *

def cargar_datos():
    # Carga pacientes y tratamientos en los Combobox
    pacientes["values"] = [f"{i[0]} - {i[1]} {i[2]}" for i in consultar("SELECT id_paciente, nombre, apellido FROM pacientes")]
    tratamientos["values"] = [f"{i[0]} - {i[2]}" for i in consultar("SELECT id_tratamiento, id_paciente, nombre_tratamiento FROM tratamientos")]

def guardar():
    if not monto.get() or not pacientes.get():
        messagebox.showwarning("Error", "Seleccione paciente y registre el monto")
        return
    
    id_pac = pacientes.get().split(" - ")[0]
    id_trat = tratamientos.get().split(" - ")[0]
    
    ejecutar("""
    INSERT INTO pagos(id_paciente, id_tratamiento, monto, fecha_pago, metodo_pago)
    VALUES(?,?,?,?,?)
    """, (id_pac, id_trat, monto.get(), fecha.get(), metodo.get()))
    
    limpiar()
    mostrar()
    messagebox.showinfo("Éxito", "Pago registrado")

def mostrar():
    tabla.delete(*tabla.get_children())
    for fila in consultar("SELECT * FROM pagos"):
        tabla.insert("", END, values=fila)

def limpiar():
    pacientes.set(""); tratamientos.set(""); monto.set(""); fecha.set(""); metodo.set("")

# Configuración
ventana = Tk()
ventana.title("Gestión de Pagos")
ventana.geometry("900x500")

# Variables
monto = StringVar(); fecha = StringVar(); metodo = StringVar()

# Formulario
frame_form = Frame(ventana)
frame_form.grid(row=0, column=0, padx=20, pady=20, sticky="n")

Label(frame_form, text="Paciente").grid(row=0, column=0, sticky="e")
pacientes = ttk.Combobox(frame_form, width=25, state="readonly")
pacientes.grid(row=0, column=1, pady=5)

Label(frame_form, text="Tratamiento").grid(row=1, column=0, sticky="e")
tratamientos = ttk.Combobox(frame_form, width=25, state="readonly")
tratamientos.grid(row=1, column=1, pady=5)

campos = [("Monto", monto), ("Fecha", fecha), ("Método Pago", metodo)]
for i, (texto, var) in enumerate(campos, 2):
    Label(frame_form, text=texto).grid(row=i, column=0, sticky="e")
    Entry(frame_form, textvariable=var).grid(row=i, column=1, pady=5)

Button(frame_form, text="Registrar Pago", command=guardar, bg="green", fg="white").grid(row=6, column=0, columnspan=2, pady=20)

# Tabla
columnas = ("ID", "ID Pac", "ID Trat", "Monto", "Fecha", "Método")
tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=100)

tabla.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

cargar_datos()
mostrar()
ventana.mainloop()
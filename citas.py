from tkinter import *
from tkinter import ttk, messagebox
from base_datos import *

# Funciones de lógica
def cargar_combos():
    try:
        pacientes["values"] = [f"{i[0]} - {i[1]}" for i in consultar("SELECT id_paciente, nombre FROM pacientes")]
        odontologos["values"] = [f"{i[0]} - {i[1]}" for i in consultar("SELECT id_odontologo, nombre FROM odontologos")]
    except Exception as e:
        messagebox.showerror("Error de Carga", f"No se pudieron cargar las listas de pacientes u odontólogos:\n{e}")

def guardar():
    if not fecha.get() or not pacientes.get():
        messagebox.showwarning("Error", "Completa los campos obligatorios (Fecha y Paciente)")
        return
    
    try:
        id_pac = pacientes.get().split(" - ")[0]
        id_odonto = odontologos.get().split(" - ")[0] if odontologos.get() else None
        
        ejecutar("""
        INSERT INTO citas(id_paciente, id_odontologo, fecha, hora, motivo, estado)
        VALUES(?,?,?,?,?,?)
        """, (id_pac, id_odonto, fecha.get(), hora.get(), motivo.get(), estado.get()))
        
        limpiar()
        mostrar()
        messagebox.showinfo("Éxito", "Cita registrada")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona un formato válido de paciente u odontólogo de la lista.")
    except Exception as e:
        messagebox.showerror("Error al Guardar", f"Ocurrió un error al guardar la cita:\n{e}")

def mostrar():
    try:
        tabla.delete(*tabla.get_children())
        for fila in consultar("SELECT * FROM citas"):
            tabla.insert("", END, values=fila)
    except Exception as e:
        messagebox.showerror("Error de Consulta", f"No se pudieron obtener los datos de las citas:\n{e}")

def limpiar():
    fecha.set(""); hora.set(""); motivo.set(""); estado.set("")

# Configuración de ventana
ventana = Tk()
ventana.title("Gestión de Citas")
ventana.geometry("900x520")

# Paleta de Colores
COLOR_FONDO = "#27FBFF"       # Celeste pastel
COLOR_LILA = "#8D3EDD"        # Lila principal
COLOR_LILA_HOVER = "#8D23F0"  # Lila al pasar el mouse
COLOR_TEXTO_BOTON = "#3B0764" # Morado oscuro para lectura clara
COLOR_PANEL = "#F0F9FF"       # Celeste muy claro para el formulario

ventana.configure(bg=COLOR_FONDO)

# Estilos ttk
style = ttk.Style()
style.theme_use("clam")

# Configuración de la tabla
style.configure("Treeview", 
                background="#FFFFFF", 
                foreground="#1E293B", 
                rowheight=26, 
                fieldbackground="#FFFFFF", 
                font=("Segoe UI", 9))
style.configure("Treeview.Heading", 
                background=COLOR_LILA, 
                foreground=COLOR_TEXTO_BOTON, 
                font=("Segoe UI", 10, "bold"))
style.map("Treeview.Heading", background=[('active', COLOR_LILA_HOVER)])
style.map("Treeview", background=[('selected', COLOR_LILA)], foreground=[('selected', '#FFFFFF')])

# Configuración de comboboxes
style.configure("TCombobox", fieldbackground="#FFFFFF", background=COLOR_LILA)

# Variables
fecha = StringVar(); hora = StringVar(); motivo = StringVar(); estado = StringVar()

# Configuración de la cuadrícula principal
ventana.columnconfigure(1, weight=1)
ventana.rowconfigure(0, weight=1)

# Formulario
frame_form = Frame(ventana, bg=COLOR_PANEL, padx=15, pady=15, highlightbackground="#BAE6FD", highlightthickness=1)
frame_form.grid(row=0, column=0, padx=20, pady=20, sticky="n")

# Estilos de etiquetas dentro del formulario
label_kwargs = {"bg": COLOR_PANEL, "fg": "#0F172A", "font": ("Segoe UI", 9, "bold")}
entry_kwargs = {"font": ("Segoe UI", 9), "relief": "solid", "bd": 1}

Label(frame_form, text="Paciente", **label_kwargs).grid(row=0, column=0, sticky="e", pady=5, padx=5)
pacientes = ttk.Combobox(frame_form, width=23, state="readonly")
pacientes.grid(row=0, column=1, pady=5, padx=5)

Label(frame_form, text="Odontólogo", **label_kwargs).grid(row=1, column=0, sticky="e", pady=5, padx=5)
odontologos = ttk.Combobox(frame_form, width=23, state="readonly")
odontologos.grid(row=1, column=1, pady=5, padx=5)

campos = [("Fecha", fecha), ("Hora", hora), ("Motivo", motivo)]
for i, (texto, var) in enumerate(campos, 2):
    Label(frame_form, text=texto, **label_kwargs).grid(row=i, column=0, sticky="e", pady=5, padx=5)
    Entry(frame_form, textvariable=var, width=25, **entry_kwargs).grid(row=i, column=1, pady=5, padx=5)

Label(frame_form, text="Estado", **label_kwargs).grid(row=5, column=0, sticky="e", pady=5, padx=5)
estado = ttk.Combobox(frame_form, values=["Pendiente", "Confirmada", "Cancelada"], width=23)
estado.grid(row=5, column=1, pady=5, padx=5)

btn_guardar = Button(
    frame_form, 
    text="Guardar Cita", 
    command=guardar, 
    bg=COLOR_LILA, 
    fg=COLOR_TEXTO_BOTON,
    activebackground=COLOR_LILA_HOVER,
    activeforeground="#FFFFFF",
    font=("Segoe UI", 10, "bold"),
    bd=0,
    padx=15,
    pady=8,
    cursor="hand2"
)
btn_guardar.grid(row=6, column=0, columnspan=2, pady=20)

# Tabla
columnas = ("ID", "ID Pac", "ID Odon", "Fecha", "Hora", "Motivo", "Estado")
tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=90, anchor="center")

tabla.grid(row=0, column=1, padx=(0, 20), pady=20, sticky="nsew")

cargar_combos()
mostrar()
ventana.mainloop()
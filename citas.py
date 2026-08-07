from tkinter import *
from tkinter import ttk, messagebox
from base_datos import *

COLOR_FONDO = "#27FBFF"
COLOR_LILA = "#8D3EDD"
COLOR_LILA_HOVER = "#983DEE"
COLOR_TEXTO_BOTON = "#3B0764"
COLOR_PANEL = "#F0F9FF"


# ✅ ESTA es la función que le faltaba al menú
def abrir_ventana():
    def cargar_combos():
        try:
            pacientes["values"] = [f"{i[0]} - {i[1]}" for i in consultar("SELECT id_paciente,nombre FROM pacientes")]
            odontologos["values"] = [f"{i[0]} - {i[1]}" for i in consultar("SELECT id_odontologo,nombre FROM odontologos")]
        except Exception as e:
            messagebox.showerror("Error de Carga", str(e))

    def guardar():
        if not fecha.get() or not pacientes.get():
            messagebox.showwarning("Error", "Completa los campos obligatorios (Fecha y Paciente)")
            return
        try:
            id_pac = pacientes.get().split(" - ")[0]
            id_od = odontologos.get().split(" - ")[0] if odontologos.get() else None
            ejecutar(
                "INSERT INTO citas(id_paciente,id_odontologo,fecha,hora,motivo,estado) VALUES(?,?,?,?,?,?)",
                (id_pac, id_od, fecha.get(), hora.get(), motivo.get(), estado_var.get())
            )
            limpiar()
            mostrar()
            messagebox.showinfo("Éxito", "Cita registrada")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar():
        tabla.delete(*tabla.get_children())
        for f in consultar("SELECT * FROM citas"):
            tabla.insert("", END, values=f)

    def limpiar():
        fecha.set("")
        hora.set("")
        motivo.set("")
        estado_var.set("")
        pacientes.set("")
        odontologos.set("")

    # === CREACIÓN DE LA VENTANA ===
    ventana = Tk()
    ventana.title("Gestión de Citas")
    ventana.geometry("900x500")
    ventana.configure(bg=COLOR_FONDO)

    st = ttk.Style()
    st.theme_use("clam")
    st.configure("Treeview.Heading", background=COLOR_LILA, foreground="white")
    st.map("Treeview.Heading", background=[("active", COLOR_LILA_HOVER)])

    fecha = StringVar()
    hora = StringVar()
    motivo = StringVar()
    estado_var = StringVar()

    f = Frame(ventana, bg=COLOR_PANEL, bd=2, relief="groove")
    f.grid(row=0, column=0, padx=20, pady=20)

    Label(f, text="Paciente", bg=COLOR_PANEL, font=("Arial", 10, "bold")).grid(row=0, column=0)
    pacientes = ttk.Combobox(f, state="readonly", width=25)
    pacientes.grid(row=0, column=1)

    Label(f, text="Odontólogo", bg=COLOR_PANEL, font=("Arial", 10, "bold")).grid(row=1, column=0)
    odontologos = ttk.Combobox(f, state="readonly", width=25)
    odontologos.grid(row=1, column=1)

    for i, (t, v) in enumerate([("Fecha", fecha), ("Hora", hora), ("Motivo", motivo)], 2):
        Label(f, text=t, bg=COLOR_PANEL, font=("Arial", 10, "bold")).grid(row=i, column=0)
        Entry(f, textvariable=v, width=28).grid(row=i, column=1)

    Label(f, text="Estado", bg=COLOR_PANEL, font=("Arial", 10, "bold")).grid(row=5, column=0)
    estado = ttk.Combobox(f, textvariable=estado_var, values=["Pendiente", "Confirmada", "Cancelada"], state="readonly", width=25)
    estado.grid(row=5, column=1)

    Button(
        f, text="Guardar Cita", command=guardar,
        bg=COLOR_LILA, fg=COLOR_TEXTO_BOTON,
        activebackground=COLOR_LILA_HOVER, activeforeground="white"
    ).grid(row=6, column=0, columnspan=2, pady=20)

    cols = ("ID", "ID Pac", "ID Odon", "Fecha", "Hora", "Motivo", "Estado")
    tabla = ttk.Treeview(ventana, columns=cols, show="headings")
    for c in cols:
        tabla.heading(c, text=c)
        tabla.column(c, width=100, anchor=CENTER)
    tabla.grid(row=0, column=1, padx=20, pady=20)

    cargar_combos()
    mostrar()

    ventana.mainloop()
from tkinter import *
from tkinter import ttk, messagebox
from base_datos import *

COLOR_FONDO = "#27FBFF"
COLOR_LILA = "#8D3EDD"
COLOR_LILA_HOVER = "#983DEE"
COLOR_TEXTO_BOTON = "#3B0764"
COLOR_PANEL = "#F0F9FF"


# ✅ Función que el menú principal llama
def abrir_ventana():

    def cargar_pacientes():
        try:
            pacientes["values"] = [f"{i[0]} - {i[1]} {i[2]}" for i in consultar("SELECT id_paciente, nombre, apellido FROM pacientes")]
        except Exception as e:
            messagebox.showerror("Error", f"No fue posible cargar los pacientes.\n\n{e}")


    def guardar():
        try:
            if not nombre.get() or not pacientes.get():
                messagebox.showwarning("Error", "El nombre del tratamiento y el paciente son obligatorios")
                return
            id_pac = pacientes.get().split(" - ")[0]
            ejecutar("""INSERT INTO tratamientos(id_paciente,nombre_tratamiento,descripcion,costo,fecha_inicio,fecha_fin)
            VALUES(?,?,?,?,?,?)""", (id_pac, nombre.get(), desc.get(), costo.get(), f_inicio.get(), f_fin.get()))
            limpiar()
            mostrar()
            messagebox.showinfo("Éxito", "Tratamiento registrado")
        except IndexError:
            messagebox.showerror("Error", "Seleccione un paciente válido.")
        except ValueError:
            messagebox.showerror("Error", "Verifique que los datos ingresados tengan el formato correcto.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al registrar el tratamiento.\n\n{e}")


    def mostrar():
        try:
            tabla.delete(*tabla.get_children())
            for fila in consultar("SELECT * FROM tratamientos"):
                tabla.insert("", END, values=fila)
        except Exception as e:
            messagebox.showerror("Error", f"No fue posible mostrar los tratamientos.\n\n{e}")


    def limpiar():
        try:
            pacientes.set("")
            nombre.set("")
            desc.set("")
            costo.set("")
            f_inicio.set("")
            f_fin.set("")
        except Exception as e:
            messagebox.showerror("Error", f"No fue posible limpiar los campos.\n\n{e}")


    # ==========================
    # VENTANA Y CONTROLES
    # ==========================
    try:
        ventana = Tk()
        ventana.title("Gestión de Tratamientos")
        ventana.geometry("1000x500")
        ventana.configure(bg=COLOR_FONDO)

        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Treeview", background="white", foreground="black", fieldbackground="white", rowheight=25)
        estilo.configure("Treeview.Heading", background=COLOR_LILA, foreground="white", font=("Arial", 10, "bold"))
        estilo.map("Treeview.Heading", background=[("active", COLOR_LILA_HOVER)])

        nombre = StringVar()
        desc = StringVar()
        costo = StringVar()
        f_inicio = StringVar()
        f_fin = StringVar()

        frame_form = Frame(ventana, bg=COLOR_PANEL, bd=2, relief="groove")
        frame_form.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        Label(frame_form, text="Paciente", bg=COLOR_PANEL, font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="e")
        pacientes = ttk.Combobox(frame_form, width=25, state="readonly")
        pacientes.grid(row=0, column=1, pady=5)

        campos = [
            ("Nombre Tratamiento", nombre),
            ("Descripción", desc),
            ("Costo", costo),
            ("F. Inicio", f_inicio),
            ("F. Fin", f_fin)
        ]
        for i, (texto, var) in enumerate(campos, 1):
            Label(frame_form, text=texto, bg=COLOR_PANEL, font=("Arial", 10, "bold")).grid(row=i, column=0, sticky="e", padx=5, pady=5)
            Entry(frame_form, textvariable=var, width=28).grid(row=i, column=1, padx=5, pady=5)

        Button(
            frame_form, text="Guardar Tratamiento", command=guardar,
            bg=COLOR_LILA, fg=COLOR_TEXTO_BOTON,
            activebackground=COLOR_LILA_HOVER, activeforeground="white",
            font=("Arial", 11, "bold"), relief="flat", cursor="hand2", width=22
        ).grid(row=6, column=0, columnspan=2, pady=20)

        columnas = ("ID", "ID Pac", "Nombre", "Desc", "Costo", "Inicio", "Fin")
        tabla = ttk.Treeview(ventana, columns=columnas, show="headings", height=18)
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=110, anchor=CENTER)
        tabla.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        cargar_pacientes()
        mostrar()
        ventana.mainloop()

    except Exception as e:
        messagebox.showerror("Error crítico", f"No fue posible iniciar la aplicación.\n\n{e}")
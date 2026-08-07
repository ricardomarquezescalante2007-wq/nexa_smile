from tkinter import *
from tkinter import ttk, messagebox
from base_datos import *

# ==========================
# COLORES
# ==========================
COLOR_FONDO = "#27FBFF"
COLOR_LILA = "#8D3EDD"
COLOR_LILA_HOVER = "#983DEE"
COLOR_TEXTO_BOTON = "#3B0764"
COLOR_PANEL = "#F0F9FF"


# ✅ Función que el menú principal llama
def abrir_ventana():

    def cargar_datos():
        try:
            pacientes["values"] = [
                f"{i[0]} - {i[1]} {i[2]}"
                for i in consultar("SELECT id_paciente, nombre, apellido FROM pacientes")
            ]

            tratamientos["values"] = [
                f"{i[0]} - {i[2]}"
                for i in consultar("SELECT id_tratamiento, id_paciente, nombre_tratamiento FROM tratamientos")
            ]

        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los datos.\n\n{e}")


    def guardar():
        try:
            if not monto.get() or not pacientes.get():
                messagebox.showwarning("Error", "Seleccione paciente y registre el monto")
                return

            if not tratamientos.get():
                messagebox.showwarning("Error", "Seleccione un tratamiento")
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

        except IndexError:
            messagebox.showerror("Error", "Seleccione un paciente y un tratamiento válidos.")
        except ValueError:
            messagebox.showerror("Error", "Verifique que los datos ingresados sean correctos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al registrar el pago.\n\n{e}")


    def mostrar():
        try:
            tabla.delete(*tabla.get_children())
            for fila in consultar("SELECT * FROM pagos"):
                tabla.insert("", END, values=fila)
        except Exception as e:
            messagebox.showerror("Error", f"No fue posible mostrar los pagos.\n\n{e}")


    def limpiar():
        try:
            pacientes.set("")
            tratamientos.set("")
            monto.set("")
            fecha.set("")
            metodo.set("")
        except Exception as e:
            messagebox.showerror("Error", f"No fue posible limpiar los campos.\n\n{e}")


    # ==========================
    # VENTANA Y CONTROLES
    # ==========================
    try:
        ventana = Tk()
        ventana.title("Gestión de Pagos")
        ventana.geometry("900x500")
        ventana.configure(bg=COLOR_FONDO)

        # Estilo ttk
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Treeview", background="white", foreground="black", rowheight=25, fieldbackground="white")
        estilo.configure("Treeview.Heading", background=COLOR_LILA, foreground="white", font=("Arial", 10, "bold"))
        estilo.map("Treeview.Heading", background=[("active", COLOR_LILA_HOVER)])

        # Variables
        monto = StringVar()
        fecha = StringVar()
        metodo = StringVar()

        # FORMULARIO
        frame_form = Frame(ventana, bg=COLOR_PANEL, bd=2, relief="groove")
        frame_form.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        Label(frame_form, text="Paciente", bg=COLOR_PANEL, font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="e", padx=5)
        pacientes = ttk.Combobox(frame_form, width=25, state="readonly")
        pacientes.grid(row=0, column=1, pady=5)

        Label(frame_form, text="Tratamiento", bg=COLOR_PANEL, font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="e", padx=5)
        tratamientos = ttk.Combobox(frame_form, width=25, state="readonly")
        tratamientos.grid(row=1, column=1, pady=5)

        campos = [("Monto", monto), ("Fecha", fecha), ("Método Pago", metodo)]
        for i, (texto, var) in enumerate(campos, 2):
            Label(frame_form, text=texto, bg=COLOR_PANEL, font=("Arial", 10, "bold")).grid(row=i, column=0, sticky="e", padx=5)
            Entry(frame_form, textvariable=var, width=28).grid(row=i, column=1, pady=5)

        boton = Button(
            frame_form, text="Registrar Pago", command=guardar,
            bg=COLOR_LILA, fg=COLOR_TEXTO_BOTON,
            activebackground=COLOR_LILA_HOVER, activeforeground="white",
            font=("Arial", 11, "bold"), width=20, relief="flat", cursor="hand2"
        )
        boton.grid(row=6, column=0, columnspan=2, pady=20)

        # TABLA
        columnas = ("ID", "ID Pac", "ID Trat", "Monto", "Fecha", "Método")
        tabla = ttk.Treeview(ventana, columns=columnas, show="headings", height=18)
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=100, anchor=CENTER)
        tabla.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        cargar_datos()
        mostrar()

        ventana.mainloop()

    except Exception as e:
        messagebox.showerror("Error crítico", f"No fue posible iniciar la aplicación.\n\n{e}")
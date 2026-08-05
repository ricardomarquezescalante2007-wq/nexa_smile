from tkinter import *
from tkinter import messagebox
from conexion import *

def iniciar_sesion():

    usuario = txt_usuario.get()
    contraseña = txt_contraseña.get()

    sql = """
    SELECT * FROM usuarios
    WHERE usuario=? AND contraseña=?
    """

    resultado = consultar(sql, (usuario, contraseña))

    if resultado:
        messagebox.showinfo("Acceso", "Bienvenido al sistema")
        ventana.destroy()

        # Aquí puedes abrir el menú principal
        # import menu
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")


ventana = Tk()
ventana.title("Login Nexa Smile")
ventana.geometry("350x220")
ventana.resizable(False, False)

Label(ventana, text="Usuario", font=("Arial", 11)).pack(pady=10)

txt_usuario = Entry(ventana, width=30)
txt_usuario.pack()

Label(ventana, text="Contraseña", font=("Arial", 11)).pack(pady=10)

txt_contraseña = Entry(ventana, show="*", width=30)
txt_contraseña.pack()

Button(
    ventana,
    text="Iniciar Sesión",
    bg="royalblue",
    fg="white",
    width=20,
    command=iniciar_sesion
).pack(pady=20)

ventana.mainloop()

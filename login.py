from tkinter import *
from tkinter import messagebox
import menu

def entrar():
    # Validación simple: usuario 'admin' y contraseña '1234'
    if usuario.get() == "admin" and contraseña.get() == "1234":
        ventana.destroy()
        menu.abrir_menu()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

ventana = Tk()
ventana.title("Login - Nexa Smile")
ventana.geometry("300x250")
ventana.config(bg="#d9f2ff")

Label(ventana, text="BIENVENIDO", bg="#d9f2ff", font=("Arial", 14, "bold")).pack(pady=15)

Label(ventana, text="Usuario", bg="#d9f2ff").pack()
usuario = Entry(ventana)
usuario.pack(pady=5)

Label(ventana, text="Contraseña", bg="#d9f2ff").pack()
contraseña = Entry(ventana, show="*")
contraseña.pack(pady=5)

Button(ventana, text="Entrar", command=entrar, bg="blue", fg="white", width=15).pack(pady=20)

ventana.mainloop()
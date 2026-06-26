from tkinter import *
from tkinter import messagebox
from menu import abrir_menu

def entrar():
    if usuario.get() == "admin" and contraseña.get() == "1234":
        ventana.destroy()
        abrir_menu()
    else:
        messagebox.showerror("Error", "Datos incorrectos")

ventana = Tk()
ventana.title("Login")
ventana.geometry("300x220")
ventana.config(bg="lightblue")

Label(ventana, text="NEXA SMILE", bg="lightblue",
      font=("Arial",16,"bold")).pack(pady=10)

Label(ventana, text="Usuario", bg="lightblue").pack()
usuario = Entry(ventana)
usuario.pack()

Label(ventana, text="Contraseña", bg="lightblue").pack()
contraseña = Entry(ventana, show="*")
contraseña.pack()

Button(ventana, text="Entrar",
       command=entrar,
       bg="blue",
       fg="white").pack(pady=15)

ventana.mainloop()
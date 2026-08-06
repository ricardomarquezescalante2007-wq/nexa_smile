import importlib
from tkinter import *
from tkinter import messagebox
from base_datos import crear_bd

try:
    crear_bd()
except Exception as e:
    messagebox.showerror(
        "Error",
        f"No fue posible crear la base de datos.\n\n{e}"
    )

def abrir_modulo(nombre):
    try:
        importlib.import_module(nombre)
    except Exception as e:
        messagebox.showerror(
            "Error",
            f"No fue posible abrir el módulo.\n\n{e}"
        )

def abrir_pacientes():
    abrir_modulo("pacientes")

def abrir_odontologos():
    abrir_modulo("odontologos")

def abrir_citas():
    abrir_modulo("citas")

def abrir_tratamientos():
    abrir_modulo("tratamientos")

def abrir_pagos():
    abrir_modulo("pagos")

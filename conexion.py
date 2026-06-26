import sqlite3

def conectar():
    return sqlite3.connect("nexa_smile.db")

def crear_tablas():
    con = conectar()
    cur = con.cursor()
    # Aquí puedes añadir la creación de tablas si no lo gestionas ya desde base_datos.py
    con.commit()
    con.close()
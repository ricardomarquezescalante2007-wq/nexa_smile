import sqlite3

DATABASE = "nexa_smile.db"

def obtener_conexion():
    try:
        conexion = sqlite3.connect(DATABASE)
        return conexion
    except sqlite3.Error as e:
        print("Error al conectar con la base de datos:", e)
        return None


def ejecutar(sql, datos=()):
    conexion = obtener_conexion()

    if conexion:
        cursor = conexion.cursor()
        cursor.execute(sql, datos)
        conexion.commit()
        conexion.close()


def consultar(sql, datos=()):
    conexion = obtener_conexion()

    if conexion:
        cursor = conexion.cursor()
        cursor.execute(sql, datos)
        registros = cursor.fetchall()
        conexion.close()
        return registros

    return []

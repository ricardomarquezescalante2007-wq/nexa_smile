import sqlite3

DATABASE = "nexa_smile.db"

# ==========================
# CONEXIÓN
# ==========================

def conectar():
    return sqlite3.connect(DATABASE)


# ==========================
# CREAR TABLAS
# ==========================

def crear_bd():
    con = conectar()
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS pacientes(
        id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellido TEXT,
        fecha_nacimiento TEXT,
        sexo TEXT,
        telefono TEXT,
        correo TEXT,
        direccion TEXT,
        fecha_registro TEXT)
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS odontologos(
        id_odontologo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        especialidad TEXT,
        telefono TEXT,
        correo TEXT,
        cedula_profesional TEXT)
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS citas(
        id_cita INTEGER PRIMARY KEY AUTOINCREMENT,
        id_paciente INTEGER,
        id_odontologo INTEGER,
        fecha TEXT,
        hora TEXT,
        motivo TEXT,
        estado TEXT)
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS tratamientos(
        id_tratamiento INTEGER PRIMARY KEY AUTOINCREMENT,
        id_paciente INTEGER,
        nombre_tratamiento TEXT,
        descripcion TEXT,
        costo REAL,
        fecha_inicio TEXT,
        fecha_fin TEXT)
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS pagos(
        id_pago INTEGER PRIMARY KEY AUTOINCREMENT,
        id_paciente INTEGER,
        id_tratamiento INTEGER,
        monto REAL,
        fecha_pago TEXT,
        metodo_pago TEXT)
    """)

    con.commit()
    con.close()


# ==========================
# FUNCIONES GENERALES
# ==========================

def ejecutar(sql, datos=()):
    con = conectar()
    cur = con.cursor()
    cur.execute(sql, datos)
    con.commit()
    con.close()


def consultar(sql, datos=()):
    con = conectar()
    cur = con.cursor()
    cur.execute(sql, datos)
    registros = cur.fetchall()
    con.close()
    return registros


if __name__ == "__main__":
    crear_bd()
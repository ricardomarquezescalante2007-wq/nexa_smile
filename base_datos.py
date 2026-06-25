import sqlite3

DATABASE_NAME = "nexa_smile.db"

def obtener_conexion():
    return sqlite3.connect(DATABASE_NAME)

def inicializar_base_datos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # ==========================
    # TABLA PACIENTES
    # ==========================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            fecha_nacimiento TEXT,
            sexo TEXT,
            telefono TEXT,
            correo TEXT,
            direccion TEXT,
            fecha_registro TEXT
        )
    """)

    # ==========================
    # TABLA ODONTOLOGOS
    # ==========================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS odontologos (
            id_odontologo INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            especialidad TEXT NOT NULL,
            telefono TEXT,
            correo TEXT,
            cedula_profesional TEXT
        )
    """)

    # ==========================
    # TABLA CITAS
    # ==========================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS citas (
            id_cita INTEGER PRIMARY KEY AUTOINCREMENT,
            id_paciente INTEGER NOT NULL,
            id_odontologo INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            hora TEXT NOT NULL,
            motivo TEXT,
            estado TEXT DEFAULT 'Pendiente',
            FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
            FOREIGN KEY (id_odontologo) REFERENCES odontologos(id_odontologo)
        )
    """)

    # ==========================
    # TABLA TRATAMIENTOS
    # ==========================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tratamientos (
            id_tratamiento INTEGER PRIMARY KEY AUTOINCREMENT,
            id_paciente INTEGER NOT NULL,
            nombre_tratamiento TEXT NOT NULL,
            descripcion TEXT,
            costo REAL,
            fecha_inicio TEXT,
            fecha_fin TEXT,
            FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente)
        )
    """)

    # ==========================
    # TABLA PAGOS
    # ==========================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pagos (
            id_pago INTEGER PRIMARY KEY AUTOINCREMENT,
            id_paciente INTEGER NOT NULL,
            id_tratamiento INTEGER NOT NULL,
            monto REAL NOT NULL,
            fecha_pago TEXT,
            metodo_pago TEXT,
            FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
            FOREIGN KEY (id_tratamiento) REFERENCES tratamientos(id_tratamiento)
        )
    """)

    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    inicializar_base_datos()
    print("Base de datos Nexa Smile creada correctamente.")
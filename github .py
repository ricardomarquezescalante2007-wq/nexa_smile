import database  # Importamos tu código sin modificarle nada

def menu_principal():
    # Inicializamos la base de datos al arrancar el programa
    database.inicializar_base_datos()
    
    while True:
        print("\n" + "="*30)
        print("   SISTEMA NEXA SMILE")
        print("="*30)
        print("1. Registrar nuevo paciente")
        print("2. Ver lista de pacientes")
        print("3. Agendar una cita")
        print("4. Ver próximas citas")
        print("5. Salir")
        print("="*30)
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            ver_pacientes()
        elif opcion == "3":
            agendar_cita()
        elif opcion == "4":
            ver_citas()
        elif opcion == "5":
            print("\n¡Gracias por usar Nexa Smile! Saliendo...")
            break
        else:
            print("\n[!] Opción no válida. Intenta de nuevo.")

def registrar_paciente():
    print("\n--- REGISTRAR PACIENTE ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    
    if not nombre or not apellido:
        print("[!] El nombre y apellido son obligatorios.")
        return

    # Usamos tu función para obtener la conexión
    conexion = database.obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            INSERT INTO pacientes (nombre, apellido, telefono) 
            VALUES (?, ?, ?)
        """, (nombre, apellido, telefono))
        conexion.commit()
        print(f"\n[✓] Paciente {nombre} {apellido} registrado con éxito.")
    except Exception as e:
        print(f"[!] Error al registrar: {e}")
    finally:
        conexion.close()

def ver_pacientes():
    print("\n--- LISTA DE PACIENTES ---")
    conexion = database.obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT id_paciente, nombre, apellido, telefono FROM pacientes")
    pacientes = cursor.fetchall()
    conexion.close()
    
    if not pacientes:
        print("No hay pacientes registrados.")
        return
        
    for p in pacientes:
        print(f"ID: {p[0]} | {p[1]} {p[2]} | Tel: {p[3]}")

def agendar_cita():
    print("\n--- AGENDAR CITA ---")
    try:
        id_paciente = int(input("ID del Paciente: "))
        id_odontologo = int(input("ID del Odontólogo: "))
        fecha = input("Fecha (DD/MM/AAAA): ")
        hora = input("Hora (HH:MM): ")
        motivo = input("Motivo de la consulta: ")
        
        conexion = database.obtener_conexion()
        cursor = conexion.cursor()
        
        cursor.execute("""
            INSERT INTO citas (id_paciente, id_odontologo, fecha, hora, motivo)
            VALUES (?, ?, ?, ?, ?)
        """, (id_paciente, id_odontologo, fecha, hora, motivo))
        
        conexion.commit()
        print("\n[✓] Cita agendada correctamente.")
    except ValueError:
        print("[!] Los IDs deben ser números enteros.")
    except Exception as e:
        print(f"[!] Error al agendar cita: {e}")
    finally:
        if 'conexion' in locals():
            conexion.close()

def ver_citas():
    print("\n--- PRÓXIMAS CITAS ---")
    conexion = database.obtener_conexion()
    cursor = conexion.cursor()
    
    # Un JOIN simple para ver los nombres de los pacientes junto a su cita
    cursor.execute("""
        SELECT c.id_cita, p.nombre, p.apellido, c.fecha, c.hora, c.motivo, c.estado 
        FROM citas c
        JOIN pacientes p ON c.id_paciente = p.id_paciente
    """)
    citas = cursor.fetchall()
    conexion.close()
    
    if not citas:
        print("No hay citas programadas.")
        return
        
    for c in citas:
        print(f"Cita #{c[0]} | Paciente: {c[1]} {c[2]} | Fecha: {c[3]} a las {c[4]} | Motivo: {c[5]} [{c[6]}]")

if __name__ == "__main__":
    menu_principal()
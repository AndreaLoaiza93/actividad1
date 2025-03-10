import os
import sys
import datetime

CLIENTES_DIR = "clientes"
os.makedirs(CLIENTES_DIR, exist_ok=True)

def inicializar_directorio():
    """Crea el directorio 'clientes' si no existe."""
    if not os.path.exists(CLIENTES_DIR):
        os.makedirs(CLIENTES_DIR)

def crear_cliente(nombre=None, servicio=None):
    if nombre is None:
        nombre = input("Ingrese el nombre del cliente: ").strip()
    if not nombre:
        print("El nombre del cliente no puede estar vacío.")
        return False
    
    archivo = os.path.join(CLIENTES_DIR, f"{nombre}.txt")
    if os.path.exists(archivo):
        print("El cliente ya existe.")
        return False
    
    if servicio is None:
        servicio = input("Ingrese la descripción del servicio: ").strip()
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")
    
    with open(archivo, "w", encoding="utf-8") as f:
        f.write(f"Cliente: {nombre}\n")
        f.write(f"Fecha de registro: {fecha}\n")
        f.write(f"Servicio: {servicio}\n")
    print("Cliente registrado con éxito.")
    return True

def agregar_servicio(nombre=None, servicio=None):
    if nombre is None:
        nombre = input("Ingrese el nombre del cliente: ").strip()
    if not nombre:
        print("El nombre del cliente no puede estar vacío.")
        return False
    
    archivo = os.path.join(CLIENTES_DIR, f"{nombre}.txt")
    if not os.path.exists(archivo):
        print("El cliente no existe.")
        return False
    
    if servicio is None:
        servicio = input("Ingrese la nueva solicitud de servicio: ").strip()
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")
    
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(f"Servicio: {servicio} ({fecha})\n")
    print("Servicio agregado correctamente.")
    return True

def buscar_cliente(nombre=None):
    if nombre is None:
        nombre = input("Ingrese el nombre del cliente: ").strip()
    if not nombre:
        print("El nombre del cliente no puede estar vacío.")
        return False
    
    archivo = os.path.join(CLIENTES_DIR, f"{nombre}.txt")
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            print(f.read())
        return True
    else:
        print("Cliente no encontrado.")
        return False

def main():
    inicializar_directorio()
    if len(sys.argv) > 1:
        comando = sys.argv[1]
        if comando == "crear" and len(sys.argv) > 2:
            return crear_cliente(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
        elif comando == "agregar" and len(sys.argv) > 2:
            return agregar_servicio(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
        elif comando == "ver" and len(sys.argv) > 2:
            return buscar_cliente(sys.argv[2])
        else:
            print("Uso: python gestor_clientes.py [crear|agregar|ver] <nombre> [servicio]")
            return False
    else:
        while True:
            print("\n--- Gestión de Clientes ---")
            print("1. Crear cliente")
            print("2. Agregar servicio")
            print("3. Buscar cliente")
            print("4. Salir")
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                crear_cliente()
            elif opcion == "2":
                agregar_servicio()
            elif opcion == "3":
                buscar_cliente()
            elif opcion == "4":
                print("Saliendo...")
                break
            else:
                print("Opción inválida.")

if __name__ == "__main__":
    main()

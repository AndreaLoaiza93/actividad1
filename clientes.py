import os

CLIENTES_DIR = "clientes"
os.makedirs(CLIENTES_DIR, exist_ok=True)

def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ").strip()
    if not nombre:
        print("El nombre del cliente no puede estar vacío.")
        return
    archivo = os.path.join(CLIENTES_DIR, f"{nombre}.txt")
    
    if os.path.exists(archivo):
        print("El cliente ya existe.")
    else:
        servicio = input("Ingrese la descripción del servicio: ").strip()
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(f"Cliente: {nombre}\n")
            f.write(f"Servicio: {servicio}\n")
        print("Cliente registrado con éxito.")

def agregar_servicio():
    nombre = input("Ingrese el nombre del cliente: ").strip()
    if not nombre:
        print("El nombre del cliente no puede estar vacío.")
        return
    archivo = os.path.join(CLIENTES_DIR, f"{nombre}.txt")
    
    if os.path.exists(archivo):
        servicio = input("Ingrese la nueva solicitud de servicio: ").strip()
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(f"Servicio: {servicio}\n")
        print("Servicio agregado correctamente.")
    else:
        print("El cliente no existe.")

def buscar_cliente():
    nombre = input("Ingrese el nombre del cliente: ").strip()
    if not nombre:
        print("El nombre del cliente no puede estar vacío.")
        return
    archivo = os.path.join(CLIENTES_DIR, f"{nombre}.txt")
    
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("Cliente no encontrado.")

def main():
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

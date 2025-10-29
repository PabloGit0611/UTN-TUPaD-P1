# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
# Crear el archivo con productos iniciales

with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,150,20\n")
    archivo.write("Cuaderno,500,10\n")
    archivo.write("Regla,200,15\n")

print("Archivo 'productos.txt' creado correctamente.")

#----------------------------------------------------------------------------------------------------------------------------------------
# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

# Leer y mostrar los productos del archivo
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        # Eliminar saltos de línea y separar por coma
        nombre, precio, cantidad = linea.strip().split(",")
        
        # Mostrar en el formato solicitado
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#----------------------------------------------------------------------------------------------------------------------------------------
# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

# Leer y mostrar productos existentes
with open("productos.txt", "r") as archivo:
    print("Productos actuales:")
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# nuevo producto desde teclado
print("\nIngrese un nuevo producto:")
nombre = input("Nombre: ")
precio = input("Precio: ")
cantidad = input("Cantidad: ")

# Agregar el nuevo producto al archivo (modo 'a' → append)
with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print("\nProducto agregado correctamente al archivo.")

#----------------------------------------------------------------------------------------------------------------------------------------
# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.

productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

# Mostrar la lista completa
print("Lista de productos:")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

#----------------------------------------------------------------------------------------------------------------------------------------
# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,150,20\n")
    archivo.write("Cuaderno,500,10\n")
    archivo.write("Regla,200,15\n")

print("Archivo 'productos.txt' creado correctamente.")

# Cargar productos desde el archivo en una lista de diccionarios
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

buscado = input("Ingrese el nombre del producto que desea buscar: ")

encontrado = False

for p in productos:
    if p["nombre"].lower() == buscado.lower():  # compara sin distinguir mayúsculas/minúsculas
        print(f"\nProducto encontrado:")
        print(f"Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\nEl producto no existe en la lista.")

#----------------------------------------------------------------------------------------------------------------------------------------
# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

# Supongamos que ya tenemos la lista de diccionarios 'productos'
# (por ejemplo, después de agregar, modificar o eliminar algún producto)

with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,150,20\n")
    archivo.write("Cuaderno,500,10\n")
    archivo.write("Regla,200,15\n")

print("Archivo 'productos.txt' creado correctamente.")

# Cargar productos desde el archivo en una lista de diccionarios
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

# Mostrar la lista completa
print("Lista de productos:")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
    

# Guardar los productos actualizados en el archivo
with open("productos.txt", "w") as archivo:
    for p in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)

print("Archivo 'productos.txt' actualizado correctamente.")

#----------------------------------------------------------------------------------------------------------------------------------------
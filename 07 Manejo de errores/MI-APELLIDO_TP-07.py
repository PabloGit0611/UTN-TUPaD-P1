#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {
    "banana": 1200,
    "anana": 2500,
    "melon" :3000,
    "uva": 1450
}

precios_frutas["naranja"] = 1200
precios_frutas["manzana"] = 1500
precios_frutas["pera"] = 2300

print(precios_frutas)

#------------------------------------------------------------------------------------------------------------------------------------------
#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas["banana"] = 1330
precios_frutas["manzana"] = 1700
precios_frutas["melon"] = 2800


print(precios_frutas)

#------------------------------------------------------------------------------------------------------------------------------------------
#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios

productos_frutas = list(precios_frutas.keys())

print(productos_frutas)

#------------------------------------------------------------------------------------------------------------------------------------------
#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

personas = {}

for i in range(5):
    nombre = input("Ingrese el nombre de la persona: ")
    numero = input("Ingrese el número de telefono: ")
    personas[nombre] = numero

print(personas)

#-----------------------------------------------------------------------------------------------------------------------------------------
# 5)Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra

frase = input("Ingrese una frase: ")
palabras = frase.split()

palabras_unicas = set(palabras)

print(palabras_unicas)

frecuencias = {}

for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

# Mostrar los resultados
print("Palabras únicas:")
print(palabras_unicas)

print("Frecuencia de cada palabra:")
print(frecuencias)

#Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumno1 = input("Ingrese nombre del primer alumno: ")
alumno2 = input("Ingrese nombre del segundo alumno: ")
alumno3 = input("Ingrese nombre del tercer alumno: ")

#------------------------------------------------------------------------------------------------------------------------------------------
#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno

nombre1 = input("Ingrese el primer alumno: ")

notas1 = []

for i in range(3):
    nota = int(input(f"Ingrese la nota {i+1} para el alumno {nombre1}: "))
    notas1.append(nota)
tupla1 = tuple(notas1)

nombre2 = input("Ingrese el segundo alumno: ")
notas2 = []
for i in range(3):
    nota = int(input(f"Ingrese la nota {i+1} para el alumno {nombre2}: "))
    notas2.append(nota)
tupla2 = tuple(notas2)

nombre3 = input("Ingrese el tercer alumno: ")
notas3 = []

for i in range(3):
    nota = int(input(f"Ingrese la nota {i+1} para el alumno {nombre3}: "))
    notas3.append(nota)

tupla3 = tuple(notas3)

print("Los alumnos con sus notas son los siguientes: ")
print(f"alumno {nombre1}: {tupla1} alumno {nombre2}: {tupla2} alumno {nombre3}: {tupla3}")

#------------------------------------------------------------------------------------------------------------------------------------------
# 7.Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)

parcial1 = {"carlos","martin","lorenzo","victor","macarena","valentin"}
parcial2 = {"valentin","nestor","nahuel","lorenzo","tomas","alex"}

print("Lista de alumnos que aprobaron ambos parciales: ")
for i in parcial1:
    if i in parcial2:
        print(i)

print("Lista de alumnos que aprobaron un solo parcial: ")
for i in parcial1:
    if i not in parcial2:
        print(i)
for i in parcial2:
    if i not in parcial1:
        print(i)

print("Lista de alumnos que aprobaron al menos un parcial: ")

lista_sin_repetir = parcial1.union(parcial2)

print(lista_sin_repetir)

#------------------------------------------------------------------------------------------------------------------------------------------
#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe

stock = {"Esponja":800,"Hamburguesa":3500,"Queso":800,"Encendedor":400}

opcion = 0
print(f"el stock es el siguiente: {stock}")
while opcion != 4:
    print("1:Consultar stock de un producto")
    print("2:agregar unidades al stock de un producto existente")
    print("3:Agregar un nuevo producto")
    print("4:Salir")
    opcion = int(input("Seleccione opcion: "))

    if opcion == 1:
        nombre_producto = input("Ingrese nombre del producto: ")
        if nombre_producto in stock:
            print(f"El producto {nombre_producto} tiene un stock de {stock[nombre_producto]}")
        else:
            print("No existe el producto ingresado.")
    if opcion == 2:
          nombre_producto = input("Ingrese nombre del producto que desea modificar su stock: ")
          if nombre_producto in stock:
            nueva_cantidad = int(input("Ingrese el nuevo stock para este producto: "))
            stock[nombre_producto] = nueva_cantidad
            print(f"Stock actualizado: {stock}")
          else:
            print("No existe el producto ingresado.")
    if opcion == 3:
        nombre_nuevo = input("Ingrese el nombre del nuevo producto: ")
        cantidad_nueva = int(input("Ingrese el stock para este nuevo producto: "))
        stock[nombre_nuevo] = cantidad_nueva
        print(f"Stock actualizado: {stock}")

#------------------------------------------------------------------------------------------------------------------------------------------
# 9)Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes","15:30") : "Futbol",
    ("Martes","17:00"): "Clases de yoga",
    ("Miercoles","11:30"): "Facultad",
    ("Jueves","19:00"):"Asado",
    ("Viernes","10:30"):"Skate"
}

numero = 0

while numero != 2:
  numero = int(input(("Seleccione 1 si desea consultar actividad o 2 si desea salir: ")))

  if numero == 1:
      dia_evento = input("Ingrese el dia del evento que desea conocer su actividad: ")
      hora_evento = input("Ingrese la hora del evento que desea conocer su actividad: ")
      tupla_actividad = (dia_evento , hora_evento)
      
      if tupla_actividad in agenda:
          print(f"La actividad es: {agenda[tupla_actividad]}")
      else:
          print("no se encontró la actividad")

#------------------------------------------------------------------------------------------------------------------------------------------
# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores

paises_original = {
    "Argentina":"Buenos aires",
    "Colombia":"Bogotá",
    "Chile":"Santiago",
    "Mexico":"Guadalajara"
}

paises_invertidos = {valor: clave for clave, valor in paises_original.items()}

print(f"Diccionario original: {paises_original}")
print(f"Diccionario invertido: {paises_invertidos}")

#------------------------------------------------------------------------------------------------------------------------------------------
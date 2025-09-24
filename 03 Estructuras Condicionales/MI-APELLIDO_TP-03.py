#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

EDAD = 18
edad = int (input("Ingrese su edad: "))

if edad > EDAD: 
    print("Es mayor de edad.")


#-------------------------------------------------------------------------------------------------------------------------
#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota = float(input("Por favor ingrese su nota: "))

if nota >= 6:
    print("Usted a aporbado.")
else:
    print("Usted a desaprobado.")


#-------------------------------------------------------------------------------------------------------------------------
#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

def ingresar_numero():
    numero = int(input("Ingrese un numero: "))
    
    if numero % 2 == 0:
        print("El numero es par.")
    
    else:
        print("Por favor, ingrese un numero que sea par")
        ingresar_numero()

ingresar_numero()


#-------------------------------------------------------------------------------------------------------------------------
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int (input("Por favor ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >=12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")


#-------------------------------------------------------------------------------------------------------------------------
#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

if len(contraseña) <=8:
    print("Por favor ingresa una contraseña entre 8 y 14 caracteres.")
elif len(contraseña) >= 14:
    print("Por favor ingrese una contrseña entre 8 y 14 caracteres.")
else:
    print("Ha ingresado una contraseña correcta.")


#-------------------------------------------------------------------------------------------------------------------------
#El paquete statistics de python contiene funciones que permiten tomar una lista de números
#y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es elsiguiente:
#from statistics import mode, median, mean
#mi_lista = [1,2,5,5,3]
#mean(mi_lista)
#En la documentación oficial se puede encontrar más información sobre este paquete:
#https://docs.python.org/es/3.8/library/statistics.html.
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
#forma aleatoria.


import random
import statistics as stats

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = stats.mean(numeros_aleatorios)
mediana = stats.median(numeros_aleatorios)

moda = stats.multimode(numeros_aleatorios)[0]

print("Números aleatorios:", numeros_aleatorios)
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda}")

if media > mediana > moda:
    print("La distribución tiene sesgo positivo (a la derecha).")
elif media < mediana < moda:
    print("La distribución tiene sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("La distribución no tiene sesgo.")
else:
    print("No se cumple estrictamente ningún criterio, la distribución es irregular.")


#-------------------------------------------------------------------------------------------------------------------------
#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

string = input("Ingrese una palabra o una frase: ").lower()

if string[-1] == 'a' or string[-1] == 'e' or string[-1] == 'i' or string[-1] == 'o' or string[-1] == 'u':
    print(string + '!')
else:
    print(string)


#-------------------------------------------------------------------------------------------------------------------------
#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

#*Uso de las Funciones upper(), lower() y title() en Python*
#En Python, existen varias funciones que permiten convertir strings entre mayúsculas y minúsculas. 
# A continuación, se presentan las funciones `upper()`, `lower()` y `title()`:
#*1. Función upper()*
#La función `upper()` convierte un string a mayúsculas.
#string = "Hola Mundo"
#print(string.upper())  # Salida: HOLA MUNDO
#*2. Función lower()*
#La función `lower()` convierte un string a minúsculas.
#string = "Hola Mundo"
#print(string.lower())  # Salida: hola mundo
#*3. Función title()*
#La función `title()` convierte un string a título, es decir, la primera letra de cada palabra en mayúscula y el resto en minúscula.
#string = "hola mundo"
#print(string.title())  # Salida: Hola Mundo
#*Ventajas*
#- Estas funciones son simples y fáciles de usar.
#- Permiten convertir strings entre mayúsculas y minúsculas de manera rápida y eficiente.
#*Uso en Condiciones*
#Estas funciones se pueden utilizar en condiciones para verificar si un string cumple con ciertos criterios. Por ejemplo:
#string = "Hola Mundo"
#if string.lower() == "hola mundo":
#    print("El string es igual")
#*Conclusión*
#En resumen, las funciones `upper()`, `lower()` y `title()` son herramientas útiles en Python para convertir strings entre mayúsculas y minúsculas. 
# su uso es simple y eficiente, y se pueden utilizar en una variedad de situaciones.

string = input("Ingrese su numbre: ")
opcion = int(input("Ingrese la opción 1(nombre en mayuscula), opcion 2(nombre en minuscula) u opcion 3(primer letra en mayuscula): "))

if opcion == 1:
    print(string.upper())
elif opcion == 2:
    print(string.lower())
elif opcion == 3:
    print(string.title())
else:
    print("Ingrese una opcion valida.")


#-------------------------------------------------------------------------------------------------------------------------
#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud de un terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud <6:
    print("Fuerte (puede causar daños en estructuras debiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala).")


#-------------------------------------------------------------------------------------------------------------------------
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

#hemisferio = input("¿En que hemisferio estas? (N/S): ")
#mes = int(input("Ingrese el mes (1-12): "))
#dia = int(input("Ingrese el día (1-31): "))

hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").upper()

mes = int(input("Ingrese el mes del año (1-12): "))
if not (1 <= mes <= 12):
    print("El numero ingresado no esta dentro del rango permitido.")
    mes = int(input("Ingrese un numero entre 1 y 12 inclusive: "))
print(f"El numero ingresado es: {mes}")

dia = int(input("Ingrese el día del mes (1,31): "))
if not (1 <= dia <= 31):
    print("El numero ingresado no esta dentro del rango permitido.")
    dia = int(input("Ingrese un numero entre 1 y 31 inclusive: "))
print(f"El numero ingresado es: {dia}")

if hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("La estacion del año es Invierno")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("La estacion del año es Primavera")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("La estacion del año es Verano")
    else:
        print("La estacion del año es Otoño")

elif hemisferio == 'S':
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("La estacion del año es Verano")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("La estacion del año es Otoño")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("La estacion del año es Invierno")
    else:
        print("La estacion del año es Primavera")

else:
    print("Hemisferio no valido")


#-------------------------------------------------------------------------------------------------------------------------



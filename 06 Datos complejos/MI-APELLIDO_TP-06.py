# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

# Llamar a la funcion desde el programa principal
imprimir_hola_mundo()

#-----------------------------------------------------------------------------------------------------------------------------------------
# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá 
# devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}"

# Programa principal
nombre = input("Introduzca su nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)

#-----------------------------------------------------------------------------------------------------------------------------------------
# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy[nombre] [apellido], 
# tengo [edad] años y vivo en [residencia]”. Pedir los datos al 
# usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Introduzca su nombre: ")

apellido = input("Introduzca su apellido: ")

edad = int(input("Introduzca su edad: "))

residencia = input("Introduzca donde vive: ")

informacion_personal(nombre, apellido, edad, residencia)

#-----------------------------------------------------------------------------------------------------------------------------------------
# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio 
# como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
# que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar 
# el radio al usuario y llamar ambas funciones para mostrar los resultados.
import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
radio = float(input("Por favor, ingrese el radio del círculo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es: {area:.2f}")
print(f"El perímetro del circulo es: {perimetro:.2f}")

#-----------------------------------------------------------------------------------------------------------------------------------------
# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y 
# mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return f"{horas} horas, {minutos} minutos y {segundos_restantes} segundos"

segundos = int(input("Ingrese una cantidad de segundos: "))
print(segundos_a_horas(segundos))

#-----------------------------------------------------------------------------------------------------------------------------------------
# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Por favor, ingresa un numero: "))
tabla_multiplicar(numero)

#-----------------------------------------------------------------------------------------------------------------------------------------
# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        print("No se puede dividr por cero")
    return suma, resta, multiplicacion, division

a = float(input("Ingrese el primer valor: "))
b = float(input("Ingrese el segundo valor: "))

suma, resta, multiplicacion, division = operaciones_basicas(a, b)

print("El resultado de las operaciones es: ")
print(f"Suma: {a} + {b} = {suma}")
print(f"Resta: {a} - {b} = {resta}")
print(f"Multiplicacion: {a} x {b} = {multiplicacion}")
print(f"Division: {a} / {b} = {division}")

#-----------------------------------------------------------------------------------------------------------------------------------------
# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la 
# función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Indice de masa corporal (IMC) es: {imc:.2f}")

#-----------------------------------------------------------------------------------------------------------------------------------------
# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C es equivalente a {fahrenheit:.2f}°F")

#-----------------------------------------------------------------------------------------------------------------------------------------
# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))
c = float(input("Ingresa el tercer numero: "))

promedio = calcular_promedio(a, b, c)
print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}")

#-----------------------------------------------------------------------------------------------------------------------------------------
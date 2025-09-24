#Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola mundo.")

#==========================================================================

#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input("Ingrese su numbre: ") 

print(f"Hola {nombre}.")

#==========================================================================

#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingrese su nombre y apellido: ")
edad = input("Ingrese su edad: ")
residencia= input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre}, tengo {edad} años, y vivo en {residencia}.")

#==========================================================================

#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

radio = float(input("Introduce el radio del círculo: "))

pi = 3.14159
area = pi * radio * radio
perimetro = pi * radio

print(f"El área del círculo es: {area:}")
print(f"El perímetro del círculo es: {perimetro:}")

#==========================================================================

#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale

segundos = float(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600

print(f"Esos segundos equivalen a {horas} horas.")

#==========================================================================

# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numero = int(input("Introduce un número: "))

print(f"Tabla de multiplicar del {numero}: ")

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#==========================================================================

#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Introduce el primer número (distinto de 0): "))

num2 = int(input("Introduce el segundo número (distinto de 0): "))

suma = num1 + num2 
print(f"La suma de {num1} más {num2} es: {suma}")

resta = num1 - num2
print(f"La resta de {num1} menos {num2} es: {resta}")

division = float
division = num1 / num2
print(f"La division de {num1} y {num2} es: {division}")

multiplicación = num1 * num2
print(f"La multiplicación de {num1} y {num2} es: {multiplicación}")

#==========================================================================

# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso(en kilogramos): "))

imc = peso / (altura**2) 
print(f"Su indice de masa corporal(IMC) es: {imc}")

#==========================================================================

#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

temperatura = float(input("Ingrese una temperatura en grados Celsius: "))

tempf = (9/5 * temperatura) + 32

print(f"Su equivalente en grados Fahrenheit es: {tempf}")

#==========================================================================

#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de esos números es: {promedio}")
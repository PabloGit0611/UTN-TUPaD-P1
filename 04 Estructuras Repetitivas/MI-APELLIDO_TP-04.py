#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for num in range(0,101):
    print(num)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.


numero = input("Ingrese un número entero: ")

# Si el número tiene signo negativo, quitarlo
if numero[0] == '-':
    numero = numero[1:]

contador = 0
for digito in numero:
    contador += 1

print("El número tiene", contador, "dígito(s).")

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el valor 1: "))
num2 = int(input("Ingrese el valor 2: "))

if num1 > num2:
    num1, num2 = num2, num1

suma = 0
for i in range(num1 + 1, num2):
    suma += i

print(f"La suma de los números comprendidos entre ambos valores es: {suma}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma = 0
numero = int(input("Ingrese un numero entero (0 para terminar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro numero (0 para terminar): "))

print(f"La suma total acumulada es: {suma}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_secreto = random.randint(0, 9)

intentos = 0
num_correcto = False
print("Adivina el número entre 0 y 9")

while not num_correcto:
    numero = int(input("Ingresa tu numero: "))
    intentos += 1

    if numero == numero_secreto:
        num_correcto = True
        print("Correcto, adivinaste el numero.")
    else:
        print("Incorrecto, intenta otra vez.")

print(f"Numero de intentos: {intentos}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------
# 6)Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for num in range(100,-1,-2):
    print(num)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un valor entero positivo: "))

while num < 0:
    print("El numero no puede ser negativo.")
    num = int(input("Por favor ingrese un valor entero positivo: "))

suma = 0
for i in range(0, num + 1):
    suma += i

print("La suma de los numeros entre 0 y", num, "es:", suma)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cant_num = int(input("Ingrese la cantidad de numeros con los que desea operar: "))
par = 0
impar = 0
positivo = 0 
negativo = 0
num0 = 0

for cont in range(cant_num):
    print("Ingrese el numero n°",(cont+1)) #cont+1 es para que nos muestre al usuario
    numero = int(input())
    
    if numero % 2 == 0:
        par += 1             #esto es igual a esto par = par + 1
    else:
        impar += 1
    
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1
    else:
        num += 1
    

print(f"\nLa cantidad de numeros pares son: {par}")

print(f"La cantidad de numeros impares son: {impar}")

print(f"La cantidad de numeros positivos son: {positivo}")

print(f"La cantidad de numeros negativos son: {negativo}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cantidad = 2
suma = 0

print(f"Ingrese {cantidad} números enteros:")

for cont in range(cantidad):
    print("Ingrese el numero n°",(cont+1)) #cont+1 es para que nos muestre al usuario
    numero = int(input())
    suma += numero

media = suma / cantidad

print(f"\nLa suma total es: {suma}")
print(f"La media de los {cantidad} números es: {media}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un numero entero: "))

signo = 1
if numero < 0:
    signo = -1
    numero = -numero

invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10

invertido *= signo

print(f"Numero invertido: {invertido}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------
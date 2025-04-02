#Ejercicio 01
print("Hola Mundo!")
#Ejercicio 02
nombre = input("Por favor, ingresa tu nombre: ")
print(f"Hola {nombre}!")
#Ejercicio 03
nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
#Ejercicio 04
pi = 3.141592653589793
radio = float(input("Ingresa el radio del círculo: "))
area = pi * radio**2
perimetro = 2 * pi * radio
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")
#Ejercicio 05
segundos = int(input("Ingresa la cantidad de segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60

print(f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")
#Ejercicio 06
numero = int(input("Ingresa un número: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
#Ejercicio 07
num1 = int(input("Ingresa el primer número (distinto de 0): "))
num2 = int(input("Ingresa el segundo número (distinto de 0): "))

if num1 == 0 or num2 == 0:
    print("Error: Ambos números deben ser distintos de 0.")
else:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2

    print(f"Suma: {num1} + {num2} = {suma}")
    print(f"Resta: {num1} - {num2} = {resta}")
    print(f"Multiplicación: {num1} x {num2} = {multiplicacion}")
    print(f"División: {num1} / {num2} = {division:.2f}")
#Ejercicio 08
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros(utilice . y no ,): "))

imc = peso / (altura ** 2)

print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
#Ejercicio 09
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
#Ejercicio 10
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")
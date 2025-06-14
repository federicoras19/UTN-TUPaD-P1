# -*- coding: utf-8 -*-
"""
TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN - PRÁCTICO 4: ESTRUCTURAS REPETITIVAS
Código unificado con todas las actividades (1 al 10).
"""

# ==================== ACTIVIDAD 1 ====================
# Imprimir números del 0 al 100 (uno por línea)
print("\n--- Actividad 1: Números del 0 al 100 ---")
for i in range(101):
    print(i)

# ==================== ACTIVIDAD 2 ====================
# Contar dígitos de un número ingresado
print("\n--- Actividad 2: Contar dígitos ---")
numero_act2 = input("Ingrese un número entero: ")
print(f"El número tiene {len(numero_act2)} dígitos.")

# ==================== ACTIVIDAD 3 ====================
# Sumar números entre dos valores (excluyéndolos)
print("\n--- Actividad 3: Suma entre valores ---")
inicio_act3 = int(input("Ingrese el primer número: "))
fin_act3 = int(input("Ingrese el segundo número: "))
suma_act3 = sum(range(inicio_act3 + 1, fin_act3))
print(f"La suma es: {suma_act3}")

# ==================== ACTIVIDAD 4 ====================
# Sumar números hasta ingresar 0
print("\n--- Actividad 4: Suma acumulativa ---")
total_act4 = 0
while True:
    num_act4 = int(input("Ingrese un número (0 para terminar): "))
    if num_act4 == 0:
        break
    total_act4 += num_act4
print(f"Total acumulado: {total_act4}")

# ==================== ACTIVIDAD 5 ====================
# Juego: adivinar número aleatorio (0-9)
import random
print("\n--- Actividad 5: Juego de adivinanza ---")
numero_secreto = random.randint(0, 9)
intentos_act5 = 0
while True:
    intento_act5 = int(input("Adivina el número (0-9): "))
    intentos_act5 += 1
    if intento_act5 == numero_secreto:
        print(f"¡Correcto! Intentos: {intentos_act5}")
        break

# ==================== ACTIVIDAD 6 ====================
# Números pares del 100 al 0 (decreciente)
print("\n--- Actividad 6: Pares decrecientes ---")
for i in range(100, -1, -2):
    print(i)

# ==================== ACTIVIDAD 7 ====================
# Suma desde 0 hasta un número dado
print("\n--- Actividad 7: Suma hasta N ---")
n_act7 = int(input("Ingrese un número entero positivo: "))
suma_act7 = sum(range(n_act7 + 1))
print(f"La suma es: {suma_act7}")

# ==================== ACTIVIDAD 8 ====================
# Contador de pares/impares/positivos/negativos (100 números)
print("\n--- Actividad 8: Estadísticas de números ---")
pares = impares = positivos = negativos = 0
for _ in range(5):  # Cambiar a 100 para la versión final
    num_act8 = int(input("Ingrese un número: "))
    if num_act8 % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num_act8 > 0:
        positivos += 1
    elif num_act8 < 0:
        negativos += 1
print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

# ==================== ACTIVIDAD 9 ====================
# Calcular media de 100 números
print("\n--- Actividad 9: Media de números ---")
suma_act9 = 0
for _ in range(5):  # Cambiar a 100 para la versión final
    suma_act9 += int(input("Ingrese un número: "))
print(f"Media: {suma_act9 / 5}")  # Ajustar divisor a 100

# ==================== ACTIVIDAD 10 ====================
# Invertir dígitos de un número
print("\n--- Actividad 10: Número invertido ---")
numero_act10 = input("Ingrese un número: ")
invertido_act10 = numero_act10[::-1]
print(f"Número invertido: {invertido_act10}")

print("\n¡Todas las actividades se han ejecutado!")

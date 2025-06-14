# 1) Edad y mayor de edad
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

# 2) Nota y aprobado/desaprobado
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Número par
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Categorías por edad
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Contraseña longitud
contrasena = input("Ingrese una contraseña: ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Sesgo estadístico con lista aleatoria
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")

# 7) Frase que termina con vocal
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

# 8) Transformar nombre según opción
nombre = input("Ingrese su nombre: ")
print("Opciones: 1-Mayúsculas, 2-Minúsculas, 3-Primera letra mayúscula")
opcion = input("Ingrese opción (1, 2 o 3): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida")

# 9) Clasificación de terremoto según magnitud
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:  # magnitud >= 7
    print("Extremo (puede causar graves daños a gran escala)")

# 10) Estación del año según hemisferio, mes y día
hemisferio = input("Ingrese hemisferio (N/S): ").upper()
mes = int(input("Ingrese mes (1-12): "))
dia = int(input("Ingrese día (1-31): "))

def es_fecha_entre(dia, mes, dia_ini, mes_ini, dia_fin, mes_fin):
    # Función para comparar fechas sin año
    if (mes_ini < mes_fin) or (mes_ini == mes_fin and dia_ini <= dia_fin):
        # Caso normal (no cruza año)
        return (mes > mes_ini or (mes == mes_ini and dia >= dia_ini)) and (mes < mes_fin or (mes == mes_fin and dia <= dia_fin))
    else:
        # Caso cruce año (ej: dic 21 - mar 20)
        return (mes > mes_ini or (mes == mes_ini and dia >= dia_ini)) or (mes < mes_fin or (mes == mes_fin and dia <= dia_fin))

if hemisferio == "N":
    if es_fecha_entre(dia, mes, 12, 21, 3, 20):
        estacion = "Invierno"
    elif es_fecha_entre(dia, mes, 3, 21, 6, 20):
        estacion = "Primavera"
    elif es_fecha_entre(dia, mes, 6, 21, 9, 20):
        estacion = "Verano"
    elif es_fecha_entre(dia, mes, 9, 21, 12, 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
elif hemisferio == "S":
    if es_fecha_entre(dia, mes, 12, 21, 3, 20):
        estacion = "Verano"
    elif es_fecha_entre(dia, mes, 3, 21, 6, 20):
        estacion = "Otoño"
    elif es_fecha_entre(dia, mes, 6, 21, 9, 20):
        estacion = "Invierno"
    elif es_fecha_entre(dia, mes, 9, 21, 12, 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio inválido"

print(f"Estación actual: {estacion}")

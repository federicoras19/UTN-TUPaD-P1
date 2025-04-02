peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros(utilice . y no ,): "))

imc = peso / (altura ** 2)

print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
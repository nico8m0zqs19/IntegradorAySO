def calcular_promedio(notas):
    return sum(notas) / len(notas)

notas = []

while True:
    try:
        cantidad = int(input("Cuántas notas desea ingresar?: "))
        if cantidad <= 0:
            print("Por favor, ingrese un número mayor a cero.")
            continue
        break
    except ValueError:
        print("Debe ingresar un número válido.")


for i in range(cantidad):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {i + 1}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Debe ingresar un número válido.")
 

promedio = calcular_promedio(notas)
print(f"\nEl promedio es: {promedio:.2f}")
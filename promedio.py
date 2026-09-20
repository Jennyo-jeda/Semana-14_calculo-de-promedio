def calcular_promedio(nota1, nota2, nota3):
    
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    return promedio

print("=== CÁLCULO DE PROMEDIO DE TRES NOTAS ===")

n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))

resultado = calcular_promedio(n1, n2, n3)

print(f"El promedio de las tres notas es: {resultado:.2f}")
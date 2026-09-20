# Semana-14_calculo-de-promedio
# Tarea Programación Básica - Funciones con parámetros y retorno

## Descripción

Este repositorio contiene la solución de la tarea de Programación Básica, cuyo objetivo es aplicar el uso de funciones con parámetros y retorno de valores mediante un programa sencillo.

Problema resuelto: Calcular el promedio de tres notas.

El programa solicita al usuario tres calificaciones, llama a una función que recibe esos tres valores como parámetros, calcula el promedio y devuelve el resultado mediante la palabra clave return. Finalmente, el resultado se muestra en pantalla.

## Estructura del código

El programa cumple con los siguientes requisitos obligatorios:

- Una función: calcular_promedio
- Parámetros de entrada: nota1, nota2, nota3
- Uso de return para devolver el promedio
- Llamada a la función en el flujo principal
- Muestra del resultado en pantalla

## Código fuente

```python
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
```

## Objetivos de aprendizaje

- Declarar y definir funciones en Python.
- Pasar argumentos a una función mediante parámetros.
- Retornar valores usando return.
- Integrar la función dentro del flujo principal del programa.
- Formatear la salida de datos numéricos en pantalla.

## Autor

Jenny Ojeda
- Materia: Fundamentos de Programación Básica
- Fecha de entrega: 20/09/2026

## Licencia

Este proyecto es de uso académico y educativo.

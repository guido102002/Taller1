#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) 
#y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random

#Función para generar la lista
def generar_lista(n, minimo, maximo):
    return [random.randint(minimo, maximo) for _ in range(n)]

#Funcion para sacar el cuadrado y el cubo de cada elemento de la lista random
def cuadrado_cubo(lista):
    print("Valor | Cuadrado | Cubo")
    for valor in lista:
        cuadrado = valor ** 2
        cubo = valor ** 3
        print(f"{valor:5} | {cuadrado:8} | {cubo:4}")

# Inicializar lista con 10 valores aleatorios entre 1 y 10
lista_numeros = generar_lista(10, 1, 10)
print("Lista de Números: ",lista_numeros)

# Mostrar los valores con sus cuadrados y cubos
cuadrado_cubo(lista_numeros)
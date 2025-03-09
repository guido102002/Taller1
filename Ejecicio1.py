# Fernando
#lista con las letras del abecedario
lis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 
       'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def filtrar_abecedario(lis, n):
    resultado = [letra for i, letra in enumerate(lis, start=1) if i % n != 0]
    return resultado

# Numero 
n = int(input("Ingrese un número: "))
resultado = filtrar_abecedario(lis, n)

# Lista resultante 
print("Lista resultante:", resultado)
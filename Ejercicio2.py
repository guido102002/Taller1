#fernando
vowels = ['a', 'e', 'i', 'o', 'u']
def contar_vocales(frase):
    vowels = ['a', 'e', 'i', 'o', 'u']
    frase = frase.lower()  # Convertimos la frase a minúsculas para evitar problemas con mayúsculas
    vocales_encontradas = [letra for letra in frase if letra in vowels]  # Filtramos las vocales
    
    print(f"Cantidad de vocales: {len(vocales_encontradas)}")
    print(f"Vocales encontradas: {', '.join(vocales_encontradas)}")

# Ejemplo de uso
frase = input("Ingrese una frase: ")
contar_vocales(frase)
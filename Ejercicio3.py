#Transforme la cadena El mejor regalo? El perdón... en el mejor perdón, utilizando únicamente los métodos 
# de listas que hemos visto. La nueva cadena debe guardarse en la variable nueva_frase:

def TransformarTexto():
    texto = "El mejor regalo? El perdón..."
    lista=texto.split()
    print(lista)

    lista.remove("regalo?")
    lista.pop(2)
    
    #Convertir las letras a minúsculas
    lista[0] = lista[0].lower()

    #Se convierte la lista de palabras a lista de caracteres para eliminar los puntos(...)
    nueva_lista=[list(palabra) for palabra in lista]

    #Se eliminan los puntos (...)
    nueva_lista[-1] = [caracter for caracter in nueva_lista[-1] if caracter not in ['.', '...']]

    #Se convierte la lista a una frase
    nueva_frase = " ".join(["".join(palabra) for palabra in nueva_lista])
    print("Frase convertida: ",nueva_frase)

TransformarTexto()
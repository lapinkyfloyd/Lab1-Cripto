# funcion principal
def cifrado_cesar(texto, desplazamiento):
    resultado = ""  # texto resultado

    for c in texto:  # recorrer texto
        if c.isalpha():  # es letra
            if c.islower():  # minuscula check
                # formula cesar
                resultado += chr((ord(c) - ord('a') + desplazamiento) % 26 + ord('a'))
            else:  # mayuscula check
                # formula cesar
                resultado += chr((ord(c) - ord('A') + desplazamiento) % 26 + ord('A'))
        else:  # no letra
            resultado += c  # copiar igual

    return resultado  # retorno final

# entrada usuario
texto = input("Ingrese el texto: ")  # pedir texto
desplazamiento = int(input("Ingrese el desplazamiento: "))  # pedir numero

# salida final
print("Texto cifrado:", cifrado_cesar(texto, desplazamiento))  # mostrar resultado

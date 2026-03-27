# funcion descifrar
def descifrar_cesar(texto):
    for desplazamiento in range(26):  # probar valores
        resultado = ""  # texto nuevo

        for c in texto:  # recorrer texto
            if c.isalpha():  # es letra
                if c.islower():  # minuscula check
                    # formula inversa
                    resultado += chr((ord(c) - ord('a') - desplazamiento) % 26 + ord('a'))
                else:  # mayuscula check
                    # formula inversa
                    resultado += chr((ord(c) - ord('A') - desplazamiento) % 26 + ord('A'))
            else:  # no letra
                resultado += c  # copiar igual

        # resultado correcto
        if resultado == "ale":
            print(">>> desplazamiento", desplazamiento, ":", resultado, "<--- probable")
        else:
            print("desplazamiento", desplazamiento, ":", resultado)

# texto cifrado
texto = "epi"  # mensaje entrada

# ejecutar funcion
descifrar_cesar(texto)  # iniciar proceso

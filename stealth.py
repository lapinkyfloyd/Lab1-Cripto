# importar libreria
from scapy.all import *
import time  # tiempo espera

# funcion envio
def enviar(destino, mensaje):
    seq = 1  # inicio secuencia
    identificador = 1234  # id fijo

    for letra in mensaje:  # recorrer mensaje
        data = b'ABCDEFGH' + letra.encode()  # datos paquete

        # crear paquete
        paquete = IP(dst=destino)/ICMP(type=8, id=identificador, seq=seq)/data

        send(paquete, verbose=0)  # enviar paquete

        print("enviado:", letra, "seq:", seq)  # mostrar envio

        seq += 1  # aumentar secuencia
        time.sleep(1)  # pausa envio

# mensaje cifrado
mensaje = "epi"  # texto oculto

# ejecutar envio
enviar("8.8.8.8", mensaje)  # destino google

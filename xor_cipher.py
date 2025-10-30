import random

def xor (mensaje, llave):
    return ''.join(chr(ord(mensaje[i]) ^ ord(llave[i])) for i in range(len(mensaje)))

mensaje = "buenos dias mundo"
llave = ''.join(str(random.randint(0, 1)) for _ in mensaje)
cifrado = xor(mensaje, llave)
descifrado = xor(cifrado, llave)

print(f"Mensaje original:", mensaje, "\nLlave:", llave, "\nMensaje cifrado:", cifrado, "\nMensaje descifrado:", descifrado)

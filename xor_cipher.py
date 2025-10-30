import random

def xor (mensaje, llave):
    return ''.join(chr(ord(m) ^ ord(l)) for m, l in zip(mensaje, llave))

mensaje = "buenos dias mundo"
llave = ''.join(str(random.randint(0, 1)) for _ in range(len(mensaje)))
cifrado = xor(mensaje, llave)
descifrado = xor(cifrado, llave)

print("Mensaje original:", mensaje)
print("Llave:", llave)  
print("Mensaje cifrado:", cifrado)
print("Mensaje descifrado:", descifrado)

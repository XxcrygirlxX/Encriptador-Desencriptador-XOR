mensaje = "buenos dias mundo"

llave = [0, 1] * (len(mensaje) // 2 + 1)
llave = llave[:len(mensaje)]

def xor_encriptado_desencriptado (texto, key):
    return ''.join(chr(ord(c) ^ k) for c, k in zip(texto, key))

mensaje_cifrado = xor_encriptado_desencriptado(mensaje, llave)
print("Mensaje cifrado:", mensaje_cifrado)

mensaje_descifrado = xor_encriptado_desencriptado(mensaje_cifrado, llave)
print("Mensaje descifrado:", mensaje_descifrado)

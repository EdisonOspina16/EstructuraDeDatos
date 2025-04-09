def contar_digitos(n):
    if n == 0:
        return 0
    digitos = n // 10
    return 1 + contar_digitos(digitos)

print(contar_digitos(12345))
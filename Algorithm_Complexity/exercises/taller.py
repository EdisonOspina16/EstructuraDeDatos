def eliminacion_de_dupliocados_en_una_lista(lista):

    nueva_lista = []
    for elemento in lista:
        if elemento not in nueva_lista:
            nueva_lista.append(elemento)

    return nueva_lista

lista = [4, 2, 4, 3, 2, 1, 5, 1]
print(eliminacion_de_dupliocados_en_una_lista(lista))


def buscar_numero_mayor(lista, objetivo):
    for numero in lista:
        if numero > objetivo:
            return numero


#lista = [1, 3, 5, 7, 9, 11, 15]
#print(buscar_numero_mayor(lista, 6))


from  stack import Stack

def esta_ordenada_ascendente(stack):
    """
    E1. Cree una función que reciba una pila y determine si sus elementos están ordenados ascendentemente desde el tope.
    Asuma que en la pila sólo hay  números enteros.
    """
    if stack.is_empty() or len(stack) == 1:
        return True  # Una pila vacía o con un solo elemento está "ordenada"

    # Copiamos la pila para no modificar la original
    copia = stack.stack[:]

    # Recorremos desde el tope hacia el fondo
    for i in range(len(copia) - 1, 0, -1):
        if copia[i] > copia[i - 1]:
            return False
    return True

p = Stack()
p.push(1)
p.push(2)
p.push(3)

print(esta_ordenada_ascendente(p))  # False, porque 3 (tope) → 2 → 1 es descendente

p2 = Stack()
p2.push(3)
p2.push(2)
p2.push(1)

print(esta_ordenada_ascendente(p2))  # True, porque 1 (tope) → 2 → 3 es ascendente


def parentesis_balanceado(expresion):
    pila = Stack()

    for caracter in expresion:
        if caracter == '(':
            pila.push(caracter)
        elif caracter == ')':
            if pila.is_empty():
                return False
            pila.pop()

    return pila.is_empty()

def insertar_entre(S, E):
    aux = Stack()
    insertado = False

    if S.is_empty():
        S.push(E)
        return

    anterior = S.pop()
    aux.push(anterior)

    while not S.is_empty():
        actual = S.pop()
        if not insertado and anterior < E < actual:
            aux.push(E)
            insertado = True
        aux.push(actual)
        anterior = actual

    if not insertado:
        aux.push(E)

    # Reconstruir la pila original
    while not aux.is_empty():
        S.push(aux.pop())

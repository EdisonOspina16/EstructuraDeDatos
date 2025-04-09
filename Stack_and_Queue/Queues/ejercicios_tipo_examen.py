from queue import Queue
from Stack_and_Queue.Stacks.stack import Stack


def procesar_lotes_con_tu_queue(personas_datos):
    # Usar tu clase Queue
    cola = Queue()

    # Encolar todas las personas
    for persona in personas_datos:
        cola.enqueue(persona)

    lote_num = 1

    while len(cola) > 0:
        lote = []

        # Sacar hasta 50 personas del frente de la cola
        for _ in range(min(50, len(cola))):
            persona = cola.dequeue()
            lote.append(persona)

        # Calcular la persona con menor IMC del lote
        menor = min(lote, key=lambda p: p[2] / (p[1] ** 2))  # p = (nombre, estatura, peso)
        imc = round(menor[2] / (menor[1] ** 2), 2)

        print(f"Lote {lote_num}: {menor[0]} con IMC {imc}")
        lote_num += 1


def buscar_elemento_en_pilas_en_colas(cola_pilas, elemento):
    encontrado = False
    cola_aux = Queue()

    while not cola_pilas.is_empty():
        pila = cola_pilas.dequeue()
        pila_aux = Stack()
        contiene = False

        # Revisa cada pila sin dañarla
        while not pila.is_empty():
            val = pila.pop()
            if val == elemento:
                contiene = True
            pila_aux.push(val)

        # Reconstruir la pila original
        while not pila_aux.is_empty():
            pila.push(pila_aux.pop())

        # Encolar la pila de nuevo en la cola auxiliar
        cola_aux.enqueue(pila)

        if contiene:
            encontrado = True

    # Restaurar la cola original
    while not cola_aux.is_empty():
        cola_pilas.enqueue(cola_aux.dequeue())

    return encontrado



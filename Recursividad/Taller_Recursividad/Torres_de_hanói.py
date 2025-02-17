def torres_de_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"disco {n} de {origen} a {destino}")
        return

    torres_de_hanoi(n - 1, origen, auxiliar, destino)
    print(f"disco {n} de {origen} a {destino}")

    torres_de_hanoi(n-1, auxiliar, destino, origen)


torres_de_hanoi(3, "A", "B", "C")

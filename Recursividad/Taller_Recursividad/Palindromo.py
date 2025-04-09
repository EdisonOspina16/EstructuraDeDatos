def es_palindromo(string, inicio=0, fin=None):
    if string == "":
        return "vacio"

    if fin == None:
        fin = len(string) - 1

    if inicio >= fin:
        return True

    if string[inicio] != string[fin]:
        return False

    return es_palindromo(string, inicio+1, fin-1)


print(es_palindromo("radar"))
print(es_palindromo(""))
print(es_palindromo("edison"))
print(es_palindromo("ana"))
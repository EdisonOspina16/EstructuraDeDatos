def anagramas(string, fija=""):
    if string == "":
        return "vacio"

    if len(string) == 0:
        return [fija]

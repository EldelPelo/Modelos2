def suma (lista):
    if lista ==[]:
        return 0
    else:
        return lista[0]+suma(lista[1:])

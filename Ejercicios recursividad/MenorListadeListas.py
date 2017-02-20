def menor(lista):
    if lista[0] <= lista[len(lista)-1] and len(lista)!=1:
        return menor(lista[:-1])
    else:
        if lista[0] >= lista[len(lista)-1] and len(lista)!=1:
            return menor(lista[1:])
        else:
            if len(lista) == 1:
                return lista

def sacarlistadelistas(lista):
    if len(lista) != 1:
        return menor(lista[-1])+sacarlistadelistas(lista[:-1])
    else:
        if len(lista) == 1:
            return menor(lista[0])

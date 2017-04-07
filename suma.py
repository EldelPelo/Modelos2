def retornarsuma(n):
    if n/10 == 0:
        if n%2 == 0:
            return n
        else:
            return 0
    else:
        if (n%10)%2 == 0:
            return n%10+retornarsuma(n/10)
        else:
            return retornarsuma(n/10)

def unirnumero(lista, n):
    if len(lista) == 1:
        return n+lista[0]
    else:
        return unirnumero(lista[1:],(n+lista[0])*(10**contardigitos(lista[1])))

def contardigitos(numero):
    if numero/10 == 0:
        return 1
    else:
        return 1+contardigitos(numero/10)






    
        

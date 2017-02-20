def comparar(lista):
    if lista[0]==lista[len(lista)-1] and len(lista)!=1:
        return 1
    else:
        if lista[0]!=lista[len(lista)-1] and len(lista)!=1:
            return comparar(lista[:len(lista)-1])
        else:
            if len(lista)==1:
                return 0


def iterarlista(lista):
    if comparar(lista)== 1 and len(lista)!=1:
        return False
    else:
        if comparar(lista)==0 and len(lista)!=1:
            return iterarlista(lista[1:])
        else:
            if len(lista)==1:
                return True

def veinteyuna(lista):
    if iterarlista(lista)==True:
        return sacarterminosasumar(lista)
    else:
        if iterarlista(lista)==False:
            return ""

def sacarterminosasumar(lista):
    if len(lista)!=1:
        return sumar(lista[0])+sacarterminos(lista[1:])
    else:
        if len(lista)==1:
            return sumar(lista[0])

def sumar(lista):
    if lista[0]=="J" or lista[0]=="j" or lista[0]=="Q" or lista[0]=="q" or lista[0]=="K" or lista[0]=="k":
        return 10
    else:
		if lista[0]=="A" or lista[0]=="a":
			return 11
		else:
			return lista[0]

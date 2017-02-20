def palindromo(cadena):
    if cadena[0] == cadena[len(cadena)-1] and len(cadena)!=1:
        return palindromo(cadena[1:len(cadena)-1])
    else:
        if cadena[0] != cadena[len(cadena)-1] and len(cadena)!=1:
            return "la palabra no es palindroma"
        else:
            if len(cadena)==1:
                return "la palabra es palindroma"

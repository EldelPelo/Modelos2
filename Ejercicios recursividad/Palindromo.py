'''
Created on 9/02/2017

@author: ElDelPelo
'''
def palindromo(frase):
    return frase == frase[::-1]

print(palindromo("oso"))
'''
Created on 9/02/2017

@author: ElDelPelo
'''
def potencia(m,n):
    if n==0:
        return 1
    else:
        return m * potencia(m, n-1)

print(potencia(2,2))
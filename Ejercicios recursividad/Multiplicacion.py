'''
Created on 9/02/2017

@author: ElDelPelo
'''

def multiplicacion(m,n):
    if m==0 or n==0:
        return 0;
    else:
        return m + multiplicacion(m, n-1)
        

print(multiplicacion(3, 4))
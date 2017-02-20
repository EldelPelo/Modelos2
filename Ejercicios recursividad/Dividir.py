'''
Created on 9/02/2017

@author: ElDelPelo
'''

def division(m,n):
    if n>m:
        return 0
    else:
        return division(m-n, n) + 1

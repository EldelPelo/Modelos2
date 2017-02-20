'''
Created on 9/02/2017

@author: ElDelPelo
'''

def absoluto(n):
    return n if n>0 else absoluto(n*-1)

print (absoluto(-1))
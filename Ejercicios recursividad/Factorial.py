'''
Created on 9/02/2017

@author: ElDelPelo
'''
def factorial(n):
    return 1 if n==0 else n * factorial(n-1)

print(factorial(5))
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:41:55 2021

@author: Jose Alcivar Garcia
"""

n=100
suma=n*(n+1)/2
print(suma)

suma=0
for i in range(1,n+1):
    suma+=1
print(suma)
print()
suma=sum(range(1, n+1))
print(suma)
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 19:21:13 2021

@author:Jose Alcivar Garcia 
"""

n=int(input("Ingrese número n (n>=0): "))
if n < 0 :
    print("Debe ingresar un número mayor o igual a cero")
else:
    print("{:d}!={:d}".format(n, factorial (n))) 
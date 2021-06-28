# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:25:42 2021

@author: Jose Alcivar Garcia
"""

n1= float(input("ingrese el primer numero: "))
n2= float(input("ingrese el segundo numero: "))
n3= float(input("ingrese el tercero numero: "))

if n2<n1>n3:
    print("el numero mayor es el primer numero: ",n1)
    
elif n1<n2>n3:
    print("el numero mayor es el segundo numero: ",n2)
    
elif n1<n3>n2:
    print("el numero mayor es el segundo numero: ",n3)
    
else: 
    print("todos los numeros son iguales")
    

    